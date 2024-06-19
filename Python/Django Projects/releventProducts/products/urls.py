from django.urls import path
from . import views

urlpatterns = [
    path('relevant_products/',views.relevantProd, name="relevantProd")
]