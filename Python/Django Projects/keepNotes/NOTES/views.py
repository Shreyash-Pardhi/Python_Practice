from django.shortcuts import render, redirect
from .models import Notes
from .forms import NoteFrom
# Create your views here.
def home(req):
    notes = Notes.objects.all()
    data = {"notes":notes}
    return render(req, 'home.html', data)

def newNote(req):
    form = NoteFrom
    if req.method == 'POST':
        form = NoteFrom(req.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        
    data = {'form':form}
    return render(req, 'newNote.html', data)

def editNote(req, _id):
    note = Notes.objects.get(id = _id)
    form = NoteFrom(instance=note)
    if req.method == 'POST':
        form = NoteFrom(req.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect('home')
    data = {'form':form}
    return render(req, 'newNote.html', data)

def deleteNote(req, _id):
    note = Notes.objects.get(id = _id)
    if(req.method == 'POST'):
        note.delete()
        return redirect('home')
    return render(req, 'deleteNote.html', {'no_te':note})
        
        