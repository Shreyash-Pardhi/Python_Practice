from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUSER, name='register'),
    path('login/', views.loginUSER, name='login'),
    path('logout/', views.logoutUSER, name='logout'),
    
    path('Home/', views.getAllProd, name='Home'),
    path('addProduct/', views.addSingleProd, name='addSingleProd'),
    path('addProductFile/', views.addCSVfile, name='addCSVfile'),

    path('currentUser/', views.currentUser, name='currentUser'),
]