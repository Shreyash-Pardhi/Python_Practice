from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUSER, name='register'),
    path('login/', views.loginUSER, name='login'),
    path('logout/', views.logoutUSER, name='logout'),
    
    path('adminHome/', views.adminUser, name = 'adminHome'),

    path('addProduct/', views.addSingleProd, name='addSingleProd'),
    path('addProductFile/', views.addCSVfile, name='addCSVfile'),
    path('getAllProducts/', views.getAllProd, name='getAllProducts'),
    # path('searchProd/', views.searchProduct, name='searchProd')
    path('imageSearch/', views.searchByImage, name='imageSearch')
    
]
