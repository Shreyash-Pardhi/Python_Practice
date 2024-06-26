from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUSER, name='register'),
    path('login/', views.loginUSER, name='login'),
    path('addProduct/', views.addSingleProd, name='addSingleProd'),
    path('addProductFile/', views.addCSVfile, name='addCSVfile')
]
