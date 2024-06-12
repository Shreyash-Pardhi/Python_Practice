import gradio as gr
from google.cloud import vision
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\Additional-Task\\storage_key.json"

#Reading Data From Google Cloud Bucket CSV
DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Products.csv")

#features Present in database csv file
DB_features = DB['Extracted_Details_from_Image']

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
        
        #Brand
        res_logo = client.logo_detection(img)
        logos = res_logo.logo_annotations
        logo = [log.description for log in logos]
        txt = txt + f"Brand: None, " if len(logo)==0 else txt + f"Brand: {logo[0]}, "
        
        #For retriving Labels
        res_label = client.label_detection(img)
        labels = res_label.label_annotations
        label = [lab.description for lab in labels]
        txt = txt + f"Description: None, " if len(label)==0 else txt + f"Description: {str(label)}, "
        
        #For retriving Text
        res_text = client.document_text_detection(img)
        texts = res_text.text_annotations
        text = [t.description for t in texts]
        txt = txt + f"Text: None, " if len(text)==0 else txt + f"Text: {text[0]}, "
        
        #for objects
        objects = client.object_localization(image=img).localized_object_annotations
        obj = [ob.name for ob in objects]
        txt = txt + f"Objects: None" if len(obj)==0 else txt + f"Object: {obj}"
        
    except Exception as e:
        gr.Warning(f"Something happened!!!, \nPlease refresh and start again...")
    
    return check_relevent_products(txt)

def check_relevent_products(inp_features):
    try: 
        a = inp_features
        new_df = DB
        for i in range(len(DB_features)):
            b=str(DB_features[i])

            #counting words in each input
            a_cnt = Counter(a)
            b_cnt = Counter(b)

            # convert to word-vectors
            words  = list(a_cnt.keys() | b_cnt.keys())
            a_vect = [a_cnt.get(word, 0) for word in words]       
            b_vect = [b_cnt.get(word, 0) for word in words]        
            sim = cosine_similarity([a_vect], [b_vect])

            new_df.loc[i, "SIM"] = sim[0][0]

        new_df.sort_values(['SIM'], axis=0, ascending=False, inplace=True)
        name=[]
        link=[]
        for i in range(5):
            name.append(new_df.iloc[i]['product_name'])
            link.append(new_df.iloc[i]['product_url'])
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

demo.launch(debug= True)