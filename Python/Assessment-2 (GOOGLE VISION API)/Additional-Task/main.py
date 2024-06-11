import gradio as gr
from google.cloud import vision
import os
import cloudinary
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
        
        # objects = client.object_localization(image=img).localized_object_annotations
        # obj = [object_.name]
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

# def save_to_csv()


brand = gr.Text(label="Brand / Logo")
labels = gr.Text(label="Labels")
text = gr.Text(label="Text")

with gr.Blocks(title="Image-Feature Extraction",
               css="footer {visibility: hidden}"
            ) as demo:
        gr.Interface(fn= Feature_Extraction,
                        inputs=gr.Image(label='Upload Product Image',type='filepath'),
                        outputs= [brand, labels, text],
                        title="<p style='color:orange; font-size:35px'>Image Feature Extraction</p><br>",
                        description="<p style='font-size:15px'>Upload an Image, and see extracted features from image using Google Vision API.<br>Features Like; Logo Detection, Labels Detection, Text Detection.</p>",
                        allow_flagging='never',
                    )

demo.launch(debug= True)
