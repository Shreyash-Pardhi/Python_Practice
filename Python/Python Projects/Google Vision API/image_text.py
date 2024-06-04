from google.cloud import vision
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "Python Projects\\Google Vision API\\api_KEY.json"

def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    
    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    print(texts)


detect_text("Python Projects\\Google Vision API\\valo.jpg")