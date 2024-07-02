from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from google.cloud import vision
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
import requests
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import *



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Django Projects\\E_Commerce\\storage_key.json"

###################### Check Duplicate Values ######################
def checkDuplicateData(df:pd.DataFrame):
    index = []
    dup = df['product_url'].duplicated()
    for i in range(len(dup)):
        if dup[i] == True:
            index.append(i+1)
    if(len(index)!=0):
        raise ValidationError(f"Product already present, Duplicated products are at rows: {index}")
    return True

###################### Validating URLs ######################
def validateURL(urlDF):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    for url in urlDF:
        r = requests.head(url, timeout=5)
        cont_type = r.headers.get('Content-Type')
        if cont_type and 'image' in cont_type:
           continue
        else:
            raise ValidationError(f"Invalid URL entered : {url} at Index: {list(urlDF).index(url)}")
    return True

###################### Saving Data to Cloud ######################
def addProdToCloud(df:pd.DataFrame):
    DB = pd.read_csv("gs://bucket-shreyash/Product_Data/ProductDEMO.csv")
    finalDF = pd.concat([DB, df], ignore_index=True)
    checkDuplicateData(finalDF)
    finalDF.to_csv("gs://bucket-shreyash/Product_Data/ProductDEMO.csv",index=False)
    
###################### Detecting Object from imageURL ######################
# def featureExtraction(uri):
#     txt = ''
#     client = vision.ImageAnnotatorClient()
#     img = vision.Image()
#     img.source.image_uri = uri
    
#     res_label = client.label_detection(img)
#     labels = res_label.label_annotations
#     label = [lab.description for lab in labels]
    
#     #for objects
#     objects = client.object_localization(image=img).localized_object_annotations
#     obj = [ob.name for ob in objects]
#     txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj}"
#     return txt

###################### Precessing Data ######################
def preProcessData(df:pd.DataFrame):
    dfURL = df['product_url']
    if(validateURL(dfURL)==True):
        # for i in range(len(dfURL)):
        #     txt = featureExtraction(dfURL[i])
        #     df.loc[i, "objects_extracted"] = txt
        # return df
        checkDuplicateData(df)
        return df
    else:
        raise ValidationError("pre processing problem")


###################### Adding Single Product ######################
def addSingleProd(req):
    try:
        if req.method == 'POST':
            prodName = req.POST.get('prodName')
            prodLink = req.POST.get('prodLink')

            if prodName and prodLink:
                productsDF = pd.DataFrame({'product_name':[prodName], 'product_url':[prodLink]})
                data = preProcessData(productsDF)
                addProdToCloud(data)
                messages.success(req, 'Product has been added successfully')
                return redirect('adminHome')
    except Exception as e:
        messages.error(req, f'{e}')
        return redirect('adminHome')


###################### Validating CSVfile ######################
def validateCSVfile(fileCsv):
    if not fileCsv.name.endswith('.csv'):
        raise ValidationError('Please upload only a csv file')
    
    df = pd.read_csv(fileCsv, index_col=False)
    if not {'product_name','product_url'}.issubset(df.columns):
        raise ValidationError("'product_name' and 'product_url' are missing, if present please check for correct column names")
    
    validateURL(df['product_url'])
    checkDuplicateData(df)
    return df

###################### Adding CSV data ######################

def addCSVfile(req):
    try:
        if req.method == 'POST':
            csvFile = req.FILES['csvFile']
            if csvFile:
                df = validateCSVfile(csvFile)
                # data = preProcessData(df)
                addProdToCloud(df)
                messages.success(req, 'Products in CSV added to Databese')
                return redirect('adminHome')
        
    except pd.errors.EmptyDataError:
        messages.error(req, 'Uploded CSV file is Empty')
        return redirect('adminHome')
    except Exception as e:
        messages.error(req, f'Error: {e}')
        return redirect('adminHome')
    
    
###################### Get all Products from bucket ######################
@login_required(login_url='login')
def getAllProd(req):
    df = pd.read_csv("gs://bucket-shreyash/Product_Data/ProductDEMO.csv")
    df = df[::-1]
    data=[{"link":l, "name":n} for l,n in zip(df['product_url'],df['product_name'])]
    return render(req, 'UserHome.html', {'data':data}) 


###################### User Registration ######################
def registerUSER(req):
    form = forms.RegisterUser()
    if req.method == 'POST':
        form = forms.RegisterUser(req.POST)
        try:
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                a = form.cleaned_data.get('is_admin')
                print("heheheheheh: ",a)
                messages.success(req, f'{user} Registered Successfully')
                return redirect('login')
        except Exception as e:
            print(f"This is the Error: {e}")
    data = {'form':form}
    return render(req, 'Register.html',data)


###################### User Login ######################

def loginUSER(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(request=req, username=username, password=password)
        if user is not None:
            login(req, user)
            if user.is_admin:
                return redirect('adminHome')
            else:
                return redirect('getAllProducts')
                # return render(req, 'UserHome.html')
        else:
            messages.error(req, 'Invalid Credentials, Please register if not registered')
            return redirect('login')
    return render(req, 'Login.html')


###################### User Logout ######################
def logoutUSER(req):
    logout(req)
    return redirect('login')


###################### Admin Page ######################
@login_required(login_url='login')
def adminUser(req):
    if req.user.is_admin:
        print(req.user.id)
        return render(req, 'AdminHome.html')
    else:
        return HttpResponse('Page not found')