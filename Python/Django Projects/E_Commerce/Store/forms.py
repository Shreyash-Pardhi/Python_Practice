from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from . import models

class RegisterUser(UserCreationForm):
    is_admin = forms.BooleanField(initial = False, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_admin']
        