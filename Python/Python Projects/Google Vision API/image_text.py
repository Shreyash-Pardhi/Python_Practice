from google.cloud import vision
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "Python Projects\\Google Vision API\\api_KEY.json"

def detect_text(uri):
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = uri
    
    res_logo = client.logo_detection(img)
    logos = res_logo.logo_annotations
    logo = [log.description for log in logos]
    txt = txt + f"Brand: None, " if len(logo)==0 else txt + f"Brand: {logo[0]}, "


detect_text("https://m.media-amazon.com/images/I/71cy1dbMh5L._SX695_.jpg")