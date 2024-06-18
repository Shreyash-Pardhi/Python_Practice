from django.urls import path
from . import views

urlpatterns = [
    path('relevent_products/',views.releventProd)
]