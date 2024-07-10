import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\storage_key.json"

def detect_obj(uri):
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = uri
    
    objects = client.object_localization(image=img).localized_object_annotations
    obj = [ob.name for ob in objects]
    
    
    response = client.label_detection(image=img)
    labels = response.label_annotations
    label = [l.description for l in labels ]
    print(obj)
    print(label)
    
    txt = ''
    txt= list(set(obj).intersection(label)) if set(obj).intersection(label) else label[:2] if len(obj) == 0 else obj
    t = str(txt)
    return t
    

print(detect_obj("https://m.media-amazon.com/images/I/71l6+lxzbTL._AC_UL640_QL65_.jpg"))