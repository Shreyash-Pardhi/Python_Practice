import os
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Django and Angular\\E-commerce(Vision API)\\backend\\storage_key.json"

def detect_obj(uri):
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = uri
    
    objects = client.object_localization(image=img).localized_object_annotations
    obj = [ob.name for ob in objects]
    
    
    response = client.label_detection(image=img)
    labels = response.label_annotations
    txtres = client.text_detection(image=img)
    tx = txtres.text_annotations
    label = [l.description for l in labels ]
    texts = [t.description for t in tx]
    
    print("obj:",obj)
    print("lab:",label)
    print("txt: ",tx)
    
    txt = ''
    txt= list(set(obj).intersection(label)) if set(obj).intersection(label) else label[:2] if len(obj) == 0 else obj
    t = str(txt)
    return 'done'
    

print(detect_obj("https://www.hubspot.com/hs-fs/hubfs/registration%20form%20template%20by%20W3Docs.png?width=600&name=registration%20form%20template%20by%20W3Docs.png"))