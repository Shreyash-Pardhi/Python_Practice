from django.db import models
from django.contrib.auth.models import AbstractUser

# class StoreUser(models.Model):
#     username = models.CharField(max_length=20, blank=False)
#     email = models.EmailField(unique=True, blank=False)
#     password1 = models.CharField(max_length=20, blank=False)
#     password2 = models.CharField(max_length=20, blank=False)
#     is_admin = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username