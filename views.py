from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def startup(request):
    return render(request,'startup.html')

def startFundraiser(request):
    return render(request, 'startFundraiser.html')

def investor(request):
    return render(request,'investor.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
