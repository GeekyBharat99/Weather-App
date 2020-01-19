# this is my views.py file
from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def About(request):
    return render(request,"about.html")