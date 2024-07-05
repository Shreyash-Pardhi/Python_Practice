import gradio as gr
from google.cloud import vision
import os
import pandas as pd
import ast
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\Additional-Task\\storage_key.json"



#Extracting features from input image
def Input_IMG_features(img_path):
    txt=''
    try:
        if(img_path == None):
            gr.Warning("Please upload a Image")
            return txt

        #reading input image
        client = vision.ImageAnnotatorClient()
        with open(img_path, "rb") as image_file:
            content = image_file.read()
        img = vision.Image(content=content)
        
        #For retriving Labels
        res_label = client.label_detection(img)
        labels = res_label.label_annotations
        label = [lab.description for lab in labels]
        
        #for objects
        objects = client.object_localization(image=img).localized_object_annotations
        obj = [ob.name for ob in objects]
        txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
        
    except Exception as e:
        gr.Warning(f"Something happened!!!, \nPlease refresh and start again...")
    
    return check_relevent_products(txt)

def check_relevent_products(inp_features):
    try: 
        #Reading Data From Google Cloud Bucket CSV
        DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")

        #features Present in database csv file
        DB_features = DB['objects_extracted']
        
        name = []
        link = []
        inp_features = set(ast.literal_eval(inp_features))
        
        for i in range(len(DB_features)):
            DB_obj = set(ast.literal_eval(DB_features[i]))
            if len(inp_features.intersection(DB_obj)) !=0:
                name.append(DB.iloc[i]['product_name'])
                link.append(DB.iloc[i]['product_url'])
        
        if(len(link)==0):
            gr.Warning(f"No product found in dataBase, \nPlease try again later")
        
        return zip(link,name)
    except Exception as e:
        gr.Warning(f"Failed to fetch relevent products, \nPlease refresh and start again...")


text = gr.Text(label="Features")
relevent_prod = gr.Gallery(columns=1,object_fit='contain',label="Relevent Products",height=600,rows=2)


with gr.Blocks(title="Relevent Product Search",
               css="footer {visibility: hidden}"    
            ) as demo:
        gr.Interface(fn= Input_IMG_features,
                        inputs=gr.Image(label='Upload Product Image',type='filepath',height="auto"),
                        outputs= relevent_prod,
                        title="<p style='color:orange; font-size:35px'>Search Relevent Products on One Click</p><br>",
                        allow_flagging='never', 
                        submit_btn="Search"
                    )

demo.launch(debug=True)
