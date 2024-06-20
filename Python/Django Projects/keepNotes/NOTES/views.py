from django.shortcuts import render
from .models import Notes
# Create your views here.
def home(req):
    notes = Notes.objects.all()
    data = {"notes":notes}
    return render(req, 'home.html', data)

def newNote(req):
    data = {}
    return render(req, 'newNote.html', data)