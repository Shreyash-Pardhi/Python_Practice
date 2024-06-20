from django.shortcuts import render
from .models import office


# Create your views here.
def new(req):
    n = office.objects.all()
    return render(req, 'index.html', {'offices':n})

def pg1(req, pk):
    n = office.objects.get(id=pk)
    return render(req, 'page1.html', {'office':n})

