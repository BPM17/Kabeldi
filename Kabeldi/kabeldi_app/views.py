from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home page")

def Menu(request):
    return HttpResponse("This is menu view")

def Footer(request):
    return HttpResponse("This is footer view")

def Development(request):
    return HttpResponse("This is development page")

def Infrastructure(request):
    return HttpResponse("This is infrastructure page")

def TechnicalSupport(request):
    return HttpResponse("This is technical Support page")

def Contact(request):
    return HttpResponse("This is contact page")

def PrivacyNotice(request):
    return HttpResponse("This is privacy note page")

def Merchandise(request):
    return HttpResponse("This is merchandise page")
