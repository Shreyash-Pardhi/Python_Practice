from django.shortcuts import render, redirect
from . import forms

def registerUSER(req):
    form = forms.RegisterUser()
    if req.method == 'POST':
        form = forms.RegisterUser(req.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('login')
        except Exception as e:
            print(f"This is the Error: {e}")
    data = {'form':form}
    return render(req, 'Register.html',data)

def loginUSER(req):
    data = {}
    return render(req, 'Login.html', data)