from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from google.cloud import vision
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
import os
import requests
import pandas as pd
from django.core.exceptions import *
import concurrent.futures



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Python\\Django Projects\\E_Commerce\\storage_key.json"

###################### Check Duplicate Values ######################
def checkDuplicateData(df:pd.DataFrame):
    index = []
    dup = df['product_url'].duplicated()
    for i in range(len(dup)):
        if dup[i] == True:
            index.append(i+1)
    if(len(index)!=0):
        raise ValidationError(f"Product(s) already present, please recheck your inventory")
    return True

###################### Validating URLs ######################
def validateURL(urlDF):
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
    DB = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")
    finalDF = pd.concat([DB, df], ignore_index=True)
    checkDuplicateData(finalDF)
    finalDF.to_csv("gs://bucket-shreyash/Product_Data/Product_D.csv",index=False)
    
###################### Detecting Object from imageURL ######################
def featureExtraction(uri):
    # txt = ''
    client = vision.ImageAnnotatorClient()
    img = vision.Image()
    img.source.image_uri = uri
    
    res_label = client.label_detection(img)
    labels = res_label.label_annotations
    label = [lab.description for lab in labels]
    
    #for objects
    objects = client.object_localization(image=img).localized_object_annotations
    obj = [ob.name for ob in objects]
    # txt = txt + f"{label}" if len(obj)==0 else txt + f"{obj[:3]}"
    txt = list(set(obj).intersection(label)) if set(obj).intersection(label) else label[:2] if len(obj) == 0 else set(obj)
    return str(txt)

###################### Precessing Data ######################
def preProcessData(df:pd.DataFrame):
    dfURL = df['product_url']
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(featureExtraction, dfURL)
    fea = [r for r in results]
    for i in range(len(fea)):
        df.loc[i, "objects_extracted"] = fea[i]
    return df
    


###################### Adding Single Product ######################
def addSingleProd(req):
    try:
        if req.method == 'POST':
            prodName = req.POST.get('prodName')
            prodLink = req.POST.get('prodLink')

            if prodName and prodLink:
                productsDF = pd.DataFrame({'product_name':[prodName], 'product_url':[prodLink]})
                validateURL(productsDF['product_url'])
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
                data = preProcessData(df)
                addProdToCloud(data)
                messages.success(req, 'Products in CSV added to Databese')
                return redirect('adminHome')
        
    except pd.errors.EmptyDataError:
        messages.error(req, 'Uploded CSV file is Empty')
        return redirect('adminHome')
    except Exception as e:
        messages.error(req, f'Error: {e}')
        return redirect('adminHome')
    
    
###################### Get all Products from bucket ######################
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def getAllProd(req):
    search_title = 'All Products'
    df = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")
    df = df[::-1]
    data=[{"link":l, "name":n} for l,n in zip(df['product_url'],df['product_name'])]
    if req.method == 'POST':
        query = str(req.POST['search_txt']).lower()
        if df['product_name'].str.lower().str.contains(query).any():
            name = df[df['product_name'].str.lower().str.contains(query)]['product_name'].tolist()
            url = df[df['product_name'].str.lower().str.contains(query)]['product_url'].tolist()
            data=[{"link":l, "name":n} for l,n in zip(url, name)]
            search_title = query.capitalize()
        else:
            messages.success(req, "Sorry, We didn't found the product you are looking for...")
            return redirect('getAllProducts')
    return render(req, 'UserHome.html', {'data':data, 'search_title': search_title}) 


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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def adminUser(req):
    if req.user.is_admin:
        print(req.user.id)
        return render(req, 'AdminHome.html')
    else:
        return HttpResponse('Page not found')


# def searchProduct(req):
#     if req.method == 'POST':
#         query = str(req.POST['search_txt']).lower()
#         df = pd.read_csv("gs://bucket-shreyash/Product_Data/ProductDEMO.csv")
#         if df['product_name'].str.lower().str.contains(query).any():
#             name = df[df['product_name'].str.lower().str.contains(query)]['product_name'].tolist()
#             url = df[df['product_name'].str.lower().str.contains(query)]['product_url'].tolist()
#             data=[{"link":l, "name":n} for l,n in zip(url, name)]
#             return render(req, 'UserHome.html', {'data':data})
#         else:
#             pass
#     return redirect('getAllProducts')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def searchByImage(req):
    return redirect('http://127.0.0.1:7860/')