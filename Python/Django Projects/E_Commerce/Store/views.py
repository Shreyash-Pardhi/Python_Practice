from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from google.cloud import vision
import os
import requests
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import *
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Django Projects\\E_Commerce\\storage_key.json"

def checkDuplicateData(df:pd.DataFrame):
    index = []
    dup = df['product_url'].duplicated()
    for i in range(len(dup)):
        if dup[i] == True:
            index.append(i+1)
    if(len(index)!=0):
        raise ValidationError(f"Product already present, Duplicated products are at rows: {index}")
    return True

def validateURL(urlDF):
    flag = False
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    for url in urlDF:
        r = requests.head(url)
        if r.headers["content-type"] in image_formats:
           flag = True
        else:
            raise ValidationError(f"Invalid URL entered : {url} at Index: {list(urlDF).index(url)}")
    return flag

def addProdToCloud(df:pd.DataFrame):
    DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")
    finalDF = pd.concat([DB, df], ignore_index=True)
    checkDuplicateData(finalDF)
    finalDF.to_csv("gs://bucket-shreyash/Product_Data/Product_D.csv",index=False)
    

def featureExtraction(uri):
    txt = ''
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = uri
    
    res_label = client.label_detection(img)
    labels = res_label.label_annotations
    label = [lab.description for lab in labels]
    
    #for objects
    objects = client.object_localization(image=img).localized_object_annotations
    obj = [ob.name for ob in objects]
    txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
    return txt

def preProcessData(df:pd.DataFrame):
    dfURL = df['product_url']
    if(validateURL(dfURL)==True):
        for i in range(len(dfURL)):
            txt = featureExtraction(dfURL[i])
            df.loc[i, "objects_extracted"] = txt
        return df
    else:
        raise ValidationError("pre processing problem")

@csrf_exempt
def addSingleProd(req):
    try:
        if req.method == 'POST':
            prodName = req.POST.get('prodName')
            prodLink = req.POST.get('prodLink')

            if prodName and prodLink:
                productsDF = pd.DataFrame({'product_name':[prodName], 'product_url':[prodLink]})
                data = preProcessData(productsDF)
                addProdToCloud(data)
                return HttpResponse('product Added successfully')
            else:
                return HttpResponse('Failed to add product')
            
    except Exception as e:
        return HttpResponse(f'Error occoured: {e}')


def validateCSVfile(fileCsv):
    if not fileCsv.name.endswith('.csv'):
        raise ValidationError('Please upload only a csv file')
    
    df = pd.read_csv(fileCsv, index_col=False)
    if not {'product_name','product_url'}.issubset(df.columns):
        raise ValidationError("'product_name' and 'product_url' are missing, if present please check for correct column names")
    
    validateURL(df['product_url'])
    checkDuplicateData(df)
    return df

@csrf_exempt
def addCSVfile(req):
    try:
        if req.method == 'POST':
            csvFile = req.FILES['csvFile']
            if csvFile:
                df = validateCSVfile(csvFile)
                data = preProcessData(df)
                addProdToCloud(data)
                return HttpResponse(f'Added CSV data')
            else:
                return HttpResponse(f'file not uploaded')
    except Exception as e:
        if str(e) == 'csvFile':
            return HttpResponse(f'Please Enter a csv file')
        return HttpResponse(f'Error occoured: {e}')

def registerUSER(req):
    form = forms.RegisterUser()
    if req.method == 'POST':
        form = forms.RegisterUser(req.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('login')
        except Exception as e:
            print(f"This is the Error: {e}")
    data = {'form':form}
    return render(req, 'Register.html',data)

def loginUSER(req):
    data = {}
    return render(req, 'Login.html', data)