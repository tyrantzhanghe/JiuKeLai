from django.shortcuts import render


def index(request):
    return render(request,'buyer/index.html',locals())


def login(request):
    return render(request,'buyer/login.html',locals())
# Create your views here.
