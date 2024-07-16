from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUSER, name='register'),
    path('login/', views.loginUSER, name='login'),
    path('logout/', views.logoutUSER, name='logout'),
]