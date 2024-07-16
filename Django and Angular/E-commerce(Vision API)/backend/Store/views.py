from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@csrf_exempt
def registerUSER(req):
    if req.method == 'POST':
        user_data = JSONParser().parse(req)
        user_ser = RegisterSerializer(data=user_data)
        if user_ser.is_valid():
            user_ser.save()
            return JsonResponse('User Registered...', safe=False)
        return JsonResponse('Failed to register!!!', safe=False)

@csrf_exempt
def loginUSER(req):
    if req.method == 'POST':
        login_data = JSONParser().parse(req)
        login_ser = LoginSerializer(data=login_data)
        if login_ser.is_valid():
            user = login_ser.validated_data['user']
            login(req, user)
            return JsonResponse(f"logged in", safe=False)
        return JsonResponse("failed to login", safe=False)

@csrf_exempt
def logoutUSER(req):
    logout(req)
    return JsonResponse(f"Logged Out {req.user.username}", safe=False)
