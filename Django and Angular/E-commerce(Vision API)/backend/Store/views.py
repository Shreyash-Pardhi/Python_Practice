from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from django.contrib.auth import login, logout, authenticate
from google.cloud import vision
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from rest_framework.decorators import authentication_classes, permission_classes,api_view
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
import os
import requests
import pandas as pd
from django.core.exceptions import *
import concurrent.futures
from rest_framework.authtoken.models import Token

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Django and Angular\\E-commerce(Vision API)\\backend\\storage_key.json"

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
    return str(txt), str(label)

###################### Precessing Data ######################
def preProcessData(df:pd.DataFrame):
    dfURL = df['product_url']
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(featureExtraction, dfURL)
    fea = [r for r in results]
    
    for i in range(len(fea)):
        df.loc[i, ["object","label"]] = fea[i][0], fea[i][1]
    return df

###################### Adding Single Product ######################
@csrf_exempt
@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def addSingleProd(req):
    try:
        if req.method == 'POST':
            input_data = JSONParser().parse(req)
            prodName = input_data['prodName']
            prodLink = input_data['prodLink']

            if prodName and prodLink:
                productsDF = pd.DataFrame({'product_name':[prodName], 'product_url':[prodLink]})
                validateURL(productsDF['product_url'])
                data = preProcessData(productsDF)
                addProdToCloud(data)
                res = {"success":True, "message":"Product has been added successfully"}
                return JsonResponse(res, safe=False)
    except Exception as e:
        res = {"success":False, "message":f'{e}'}
        return JsonResponse(res, safe=False)

###################### Validating CSVfile ######################
def validateCSVfile(fileCsv):
    if not fileCsv.name.endswith('.csv'):
        raise ValidationError('Please upload only a csv file')
    
    df = pd.read_csv(fileCsv, index_col=False)
    if len(df)==0:
        raise ValidationError("Uploded CSV file is Empty")
    
    if not {'product_name','product_url'}.issubset(df.columns):
        raise ValidationError("'product_name' and 'product_url' are missing, if present please check for correct column names")
    
    validateURL(df['product_url'])
    checkDuplicateData(df)
    return df

###################### Adding CSV data ######################
@csrf_exempt
@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def addCSVfile(req):
    try:
        if req.method == 'POST':
            csvFile = req.FILES['file']
            if csvFile:
                df = validateCSVfile(csvFile)
                data = preProcessData(df)
                addProdToCloud(data)
                res = {"success":True, "message":"Products in CSV added to Databese"}
                return JsonResponse(res, safe=False)
        
    except pd.errors.EmptyDataError:
        res = {"success":False, "message":"Uploded CSV file is Empty"}
        return JsonResponse(res, safe=False)
    except Exception as e:
        res = {"success":False, "message":f'Error: {e}'}
        return JsonResponse(res, safe=False)

###################### getAllProducts / UserHome ######################
@csrf_exempt
@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getAllProd(req):
    search_title = 'All Products'
    df = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")
    df = df[::-1]
    data = [{"link":l, "name":n} for l,n in zip(df['product_url'],df['product_name'])]
    res={"success":True, "s_title": search_title,"message":"","data":data}
    if req.method == 'POST':
        inp = JSONParser().parse(req)
        query = str(inp['search_txt']).lower()
        if df['product_name'].str.lower().str.contains(query).any():
            name = df[df['product_name'].str.lower().str.contains(query)]['product_name'].tolist()
            url = df[df['product_name'].str.lower().str.contains(query)]['product_url'].tolist()
            search_title = query.capitalize()
            data=[{"link":l, "name":n} for l,n in zip(url, name)]
            res={"success":True, "s_title": search_title,"message":f"","data":data}
        else:
            res={"success":False, "s_title": search_title,"message":"Sorry, We didn't found the product you are looking for...","data":data}
    return JsonResponse(res, safe=False)


###################### Register User ######################
@csrf_exempt
def registerUSER(req):
    if req.method == 'POST':
        user_data = JSONParser().parse(req)
        user_ser = RegisterSerializer(data=user_data)
        if user_ser.is_valid():
            user_ser.save()
            user = User.objects.get(username = user_data['username'])
            token = Token.objects.get(user=user)
            ser = RegisterSerializer(user)
            i={
                "user":ser.data,
                "token":token.key
            }

            return JsonResponse({"success":True, "message":f"{user}, you have successfully Registered..."}, safe=False)
        
        error=None
        for _, value in user_ser.errors.items():
            if isinstance(value, list) and len(value) > 0:
                error = value[0]
                break

        return JsonResponse({"success":False, "message":f"{error}"}, safe=False)


###################### Login User ######################
@csrf_exempt
def loginUSER(req):
    global usernm
    if req.method == 'POST':
        login_data = JSONParser().parse(req)
        login_ser = LoginSerializer(data=login_data)
        if login_ser.is_valid():
            user = User.objects.get(username = login_data['username'])
            ser = RegisterSerializer(user)
            token, create_token = Token.objects.get_or_create(user = user)
            login(req, user)

            res={
                "user":ser.data
            }
            res['token'] = token.key if token else create_token.key
            
            return JsonResponse({"success":True,"res":res, "u_status":user.is_admin, "message":f"{user}, Logged in successfully..."}, safe=False)
        
        error=None
        for _, value in login_ser.errors.items():
            if isinstance(value, list) and len(value) > 0:
                error = value[0]
                break
        return JsonResponse({"success":False, "message":f"{error}"}, safe=False)



###################### Logout user ######################
@csrf_exempt
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logoutUSER(req):
    try:
        req.user.auth_token.delete()
        return JsonResponse({"success":True, "message":f"{req.user}, Logged out successfully..."}, safe=False)
    except Exception as e:
        return JsonResponse({"success":False, "message":f"Unable to logout!!!\n{e}"}, safe=False)

@csrf_exempt
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def currentUser(req):
    userData = {'username':str(req.user), 'is_admin':req.user.is_admin}
    return JsonResponse({"userData": userData},safe=False)