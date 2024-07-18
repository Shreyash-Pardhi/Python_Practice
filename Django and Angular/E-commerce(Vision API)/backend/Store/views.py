from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from google.cloud import vision
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
import os
import requests
import pandas as pd
from django.core.exceptions import *
import concurrent.futures
from rest_framework.authtoken.models import Token

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Work and Assignments\\Django and Angular\\E-commerce(Vision API)\\backend\\storage_key.json"


@csrf_exempt
def getAllProd(req):
    search_title = 'All Products'
    df = pd.read_csv("gs://bucket-shreyash/Product_Data/Product_D.csv")
    df = df[::-1]
    data = [{"link":l, "name":n} for l,n in zip(df['product_url'],df['product_name'])]
    if req.method == 'POST':
        inp = JSONParser().parse(req)
        query = str(inp['search_txt']).lower()
        if df['product_name'].str.lower().str.contains(query).any():
            name = df[df['product_name'].str.lower().str.contains(query)]['product_name'].tolist()
            url = df[df['product_name'].str.lower().str.contains(query)]['product_url'].tolist()
            search_title = query.capitalize()
            data=[{"link":l, "name":n} for l,n in zip(url, name)]
            res={"success":True, "s_title": search_title,"message":"","data":data}
        else:
            res={"success":False, "s_title": search_title,"message":"Sorry, We didn't found the product you are looking for...","data":data}
    return JsonResponse(res, safe=False)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def registerUSER(req):
    if req.method == 'POST':
        user_data = JSONParser().parse(req)
        user_ser = RegisterSerializer(data=user_data)
        if user_ser.is_valid():
            user = user_ser.save()
            login(req, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"success":True, "message":f"{user_data['username']}, you have successfully registered...","token": token.key}, safe=False)
        return JsonResponse({"success":False, "message":f"Registration Failed!!, please try again..."}, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def loginUSER(req):
    if req.method == 'POST':
        login_data = JSONParser().parse(req)
        login_ser = LoginSerializer(data=login_data)
        if login_ser.is_valid():
            user = login_ser.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"success":True, "message":f"{user}, Logged in successfully...","token": token.key,}, safe=False)
        return JsonResponse({"success":False, "message":f"Failed to Log In!!!"}, safe=False)

@csrf_exempt
def logoutUSER(req):
    if req.user.is_authenticated:
        username = req.user.username
        req.user.auth_token.delete()
        logout(req)
        return JsonResponse({"success":True, "message":f"{username}, Logged out successfully..."}, safe=False)
    return JsonResponse({"success":False, "message":"No user is logged in!!!"}, safe=False)