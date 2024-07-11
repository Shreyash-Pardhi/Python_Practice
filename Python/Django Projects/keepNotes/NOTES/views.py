from django.shortcuts import render, redirect
from .models import Notes
from .forms import NoteFrom
# Create your views here.
def home(req):
    notes = Notes.objects.all()
    form = NoteFrom
    data = {"notes":notes, "form":form}
    return render(req, 'home.html', data)

def newNote(req):
    form = NoteFrom
    if req.method == 'POST':
        form = NoteFrom(req.POST)
        if form.is_valid:
            temp = form.save(commit=False)
            temp.user = req.user
            form.save()
            return redirect('home')
    data = {'form':form, 'form_action':'newNote'}
    return render(req, 'newNote.html', data)

def editNote(req, _id):
    note = Notes.objects.get(id = _id)
    form = NoteFrom(instance=note)
    if req.method == 'POST':
        form = NoteFrom(req.POST, instance=note)
        if form.is_valid:
            temp = form.save(commit=False)
            temp.user = req.user
            form.save()
            return redirect('home')
    data = {'form':form, 'form_action':'editNote'}
    return render(req, 'newNote.html', data)

def deleteNote(req, _id):
    note = Notes.objects.get(id = _id)
    if(req.method == 'POST'):
        note.delete()
        return redirect('home')
    return render(req, 'deleteNote.html', {'no_te':note})
        
        