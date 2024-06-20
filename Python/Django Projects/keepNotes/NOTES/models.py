from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(blank=False)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.note
    