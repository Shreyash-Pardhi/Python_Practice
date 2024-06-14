from django.shortcuts import render
from django.http import HttpResponse
from google.cloud import vision
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Assessment-2 (GOOGLE VISION API)\\Additional-Task\\storage_key.json"

DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Products.csv")

#features Present in database csv file
DB_features = DB['Extracted_Details_from_Image']

def Input_IMG_features(img_path):
    txt=''
    try:
        if(img_path == None):
            # gr.Warning("Please upload a Image")
            print("enter path")
            return txt

        #reading input image
        client = vision.ImageAnnotatorClient()
        # with open(img_path, "rb") as image_file:
        #     content = image_file.read()
        # img = vision.Image(content=content)
        
        img = vision.Image()
        img.source.image_uri = img_path
        
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
        # gr.Warning(f"Something happened!!!, \nPlease refresh and start again...")
        print('Exception')
    
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
            words  = list(a_cnt.keys() & b_cnt.keys())
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
        return link, name
    except Exception as e:
        # gr.Warning(f"Failed to fetch relevent products, \nPlease refresh and start again...")
        print("failed to fetch product")
        
# Create your views here.

def greet(req):
    if req.method == 'POST':
        uri = req.POST.get("url_Link")
        param = "https://5.imimg.com/data5/ANDROID/Default/2021/7/VD/GM/DZ/44196072/product-jpeg-1000x1000.jpg" if(uri==None) else uri
        li,nam = Input_IMG_features(param)
        return render(req, 'index.html',{"imglink": li, "names": nam})
    else:
        return render(req, template_name='index.html')
    
