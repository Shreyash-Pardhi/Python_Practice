from django.forms import ModelForm
from .models import Notes

class NoteFrom(ModelForm):
    class Meta:
        model = Notes
        fields = ['note']