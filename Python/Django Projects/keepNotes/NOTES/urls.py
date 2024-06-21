from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('newNote/', views.newNote, name='newNote'),
    path('editNote/<str:_id>/', views.editNote, name='editNote'),
    path('deleteNote/<str:_id>/', views.deleteNote, name='deleteNote')
]
