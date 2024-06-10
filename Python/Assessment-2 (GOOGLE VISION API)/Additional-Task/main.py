import gradio as gr
from google.cloud import vision
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\Additional-Task\\storage_key.json"

def Feature_Extraction(img_path):
    l=lbl=txt=''
    try:
        if(img_path == None):
            gr.Warning("Please upload a Image")
            return (l,lbl,txt)
     
        client = vision.ImageAnnotatorClient()
        with open(img_path, "rb") as image_file:
            content = image_file.read()
        img = vision.Image(content=content)
        
        #Brand
        res_logo = client.logo_detection(img)
        logos = res_logo.logo_annotations
        logo = [log.description for log in logos]
        l = f"Brand not detected!!" if len(logo)==0 else f"{logo[0]}"
        
        #For retriving Labels
        res_label = client.label_detection(img)
        labels = res_label.label_annotations
        label = [lab.description for lab in labels]
        lbl =f"Labels not detected!!" if len(label)==0 else f"{",  ".join(label)}"
        
        #For retriving Text
        res_text = client.document_text_detection(img)
        texts = res_text.text_annotations
        text = [t.description for t in texts]
        txt = f"Text not detected!!" if len(text)==0 else f"{text[0]}"
        
    except Exception as e:
        gr.Warning(f"Something happened!!!, \nPlease refresh and start again...")
    
    return (l,lbl,txt)
    
        
brand = gr.Text(label="Brand")
labels = gr.Text(label="Labels")
text = gr.Text(label="Text")

demo = gr.Interface(fn= Feature_Extraction,
                    inputs=gr.Image(label='Product Image',type='filepath'),
                    outputs= [brand, labels, text],
                    title="Image Feature Extraction",
                    description="Upload an Image, and see extracted features from image using Google Vision API.<p>Features Like; Logo Detection, Labels Detection, Text Detection.</p>",
                    allow_flagging='never',
                    css="footer {visibility: hidden}")

demo.launch(debug= True)
