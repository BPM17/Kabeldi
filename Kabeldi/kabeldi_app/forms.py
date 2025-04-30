from django import forms
from .models import ContactForm

class Client(forms.ModelForm): 
    class Meta:
        model = ContactForm
        fields = ['name', 'cellphone', 'email', 'description']