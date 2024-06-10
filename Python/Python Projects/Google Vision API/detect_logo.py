import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\storage_key.json"

# def detect_logos(path):

#     client = vision.ImageAnnotatorClient()

#     with open(path, "rb") as image_file:
#         content = image_file.read()
        
#     image = vision.Image(content=content)

#     res_logo = client.logo_detection(image)
#     res_text = client.document_text_detection(image)
#     res_loc = client.landmark_detection(image)
    
#     logos = res_logo.logo_annotations
#     texts = res_text.text_annotations
#     landmarks = res_loc.landmark_annotations
    
#     logos = res_logo.logo_annotations
#     text = [txt.description for txt in texts]
#     landmark = [loc.description for loc in landmarks]
    
#     print(content)
#     # print("Logos : ",logo)
#     # print("Texts : ",text[0])
#     # print("Landmark/Location: ", landmark)
    


# detect_logos("D:\\Work and Assignments\\Python\\Python Projects\\Google Vision API\\mahindra.jpg")


def detect_text(uri):
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = uri
    
    res_logo = client.logo_detection(img)
    logos = res_logo.logo_annotations
    logo = [log.description for log in logos]
    print((img.source.image_uri))


detect_text("https://m.media-amazon.com/images/I/71cy1dbMh5L._SX695_.jpg")