from django.shortcuts import render
from google.cloud import vision
import os
import pandas as pd
import requests
import ast
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\Additional-Task\\storage_key.json"
error = "Please enter the valid URL to proceed"

#Reading Data From Google Cloud Bucket CSV
DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Products_v2.csv")

#features Present in database csv file
DB_features = DB['objects_extracted']

#Extracting features from input image
def Input_IMG_features(img_path):
    global error
    txt=''  
    try:
        #reading input image
        client = vision.ImageAnnotatorClient()
        img = vision.Image()
        img.source.image_uri = img_path
        #For retriving Labels
        res_label = client.label_detection(img)
        labels = res_label.label_annotations
        label = [lab.description for lab in labels]
        
        #for objects
        objects = client.object_localization(image=img).localized_object_annotations
        obj = [ob.name for ob in objects]
        txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
        
    except Exception as e:
        error = "Something happened!!!, \nPlease refresh and start again..."
    
    return check_relevent_products(txt)

def check_relevent_products(inp_features):
    global error
    try: 
        name = []
        link = []
        inp_features = set(ast.literal_eval(inp_features))
        
        for i in range(len(DB_features)):
            DB_obj = set(ast.literal_eval(DB_features[i]))
            if len(inp_features.intersection(DB_obj)) !=0:
                name.append(DB.iloc[i]['product_name'])
                link.append(DB.iloc[i]['product_url'])
        
        return link,name
    except Exception as e:
        error = "Failed to fetch relevent products, \nPlease refresh and start again..."
        

def is_url_image(image_url):
    try: 
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        r = requests.head(image_url)
        if r.headers["content-type"] in image_formats:
           return True
        return False
    except Exception as e:
        return False

def releventProd(req):
    if req.method == 'POST':
        uri = req.POST.get("url_Link")
        if(uri=='' or is_url_image(uri)==False):
            return render(req,'initial.html', {"erro": error})
        li,nam = Input_IMG_features(uri)
        items = [{"link":l, "name":n} for l,n in zip(li,nam)]
        if len(li)==0:
            return render(req,'initial.html', {"erro": "No product found in dataBase, Please try again later"})
        return render(req, 'index.html',{"data": items})
    else:
        return render(req,'initial.html')