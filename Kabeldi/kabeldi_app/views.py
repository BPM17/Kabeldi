from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm


# Create your views here.
def Menu(request):
    return render(request, 'header.html')

def Footer(request):
    return render(request, 'footer.html')

def index(request):
    return render(request, 'index.html')

def Development(request):
    return render(request, 'development.html')

def Infrastructure(request):
    return render(request, 'infrastructure.html')

def TechnicalSupport(request):
    return render(request, 'technicalSupport.html')

def Contact(request):
    return render(request, 'contact.html')

def PrivacyNotice(request):
    return render(request, 'privacyNotice.html')

def Merchandise(request):
    return render(request, 'merchandise.html')