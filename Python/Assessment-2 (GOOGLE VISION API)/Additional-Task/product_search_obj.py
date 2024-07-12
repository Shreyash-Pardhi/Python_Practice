import gradio as gr
from google.cloud import vision
import os
import pandas as pd
import ast
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\Additional-Task\\storage_key.json"



#Extracting features from input image
def Input_IMG_features(img_path):
    txt=''
    l=''
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
        l+=f"{label}"
        #for objects
        objects = client.object_localization(image=img).localized_object_annotations
        obj = [ob.name for ob in objects]
        txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
        
    except Exception as e:
        gr.Warning(f"Something happened!!!, \nPlease refresh and start again...")
    
    return check_relevent_products(txt, l)

def rel(df: pd.DataFrame, inp):
    def cal(bl: set, tl: set):
        i = bl.intersection(tl)
        u = bl.union(tl)
        return len(i) / len(u) if u else 0.0
    
    scr = [
        (df.iloc[i]['product_name'], df.iloc[i]['product_url'], 
         cal(set(ast.literal_eval(df.iloc[i]['label'])), inp))
        for i in range(len(df))
    ]

    return sorted(scr, key=lambda x: x[2], reverse=True)

def check_relevent_products(inp_features, lbl):
    try: 
        #Reading Data From Google Cloud Bucket CSV
        DB = pd.read_csv("D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\results.csv")
        #features Present in database csv file
        DB_features = DB['object']
        inp_features = set(ast.literal_eval(inp_features))
        lbl = set(ast.literal_eval(lbl))
        
        data = [len(inp_features.intersection(set(ast.literal_eval(feature)))) > 0 for feature in DB_features]
        new_df = DB[data][['product_name', 'product_url', 'label']].reset_index(drop=True)
        final = rel(new_df, lbl)
        
        name, link = zip(*[(n, l) for n, l, _ in final])
        
        if(len(link)==0):
            gr.Warning(f"No product found in dataBase, \nPlease try again later")
        
        return zip(link,name)
    except Exception as e:
        gr.Warning(f"Failed to fetch relevent products, \nPlease refresh and start again...")


text = gr.Text(label="Features")
relevent_prod = gr.Gallery(columns=1,object_fit='contain',label="Relevent Products",height=600)


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
        
        gr.HTML("""
        <style>
            img{
                background-color: white;
            }
        </style>
        """)

demo.launch(debug=True)