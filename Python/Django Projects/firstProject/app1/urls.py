from django.urls import path
from . import views


urlpatterns = [
    path('',views.new, name='home'),
    path('p1/<str:pk>',views.pg1, name='p1'),
]