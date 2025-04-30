from django import forms
from .models import ContactForm

class Client(forms.ModelForm): 
    class Meta:
        model = ContactForm
        fields = ['name', 'cellphone', 'email', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'formControl', 'placeholder': 'Correo'}),
            'cellphone': forms.TextInput(attrs={'class': 'formControl', 'placeholder': 'Teléfono'}),
            'description': forms.Textarea(attrs={'class': 'formControl', 'rows': 4}),
        }