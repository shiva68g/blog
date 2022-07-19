from .models import modelblogs
from django.shortcuts import render

def home(req):
    data = 'sign up/sign in'
    if req.user.is_authenticated:
        data = 'log out'
    blo = modelblogs.objects.all()
    return render(req , "home.html" , {'data':data , 'blogs':blo});


def blogs(req):
    data = 'sign up/sign in'
    if req.user.is_authenticated:
        data = 'log out'
    blo = modelblogs.objects.all()
    return render(req , "blogs.html" , {'data':data , 'blogs':blo})