from django import forms

class Client(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Introduce tu nombre','class': 'input'}))
    telephone = forms.IntegerField(label="Teléfono", max_value=15,widget=forms.TextInput(attrs={'placeholder':'Introduce tu número de telefono','class': 'input'}))
    email = forms.EmailField(label="E-mail", max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu correo electrónico','class': 'input'}))
    description = forms.CharField(label="Descripción", max_length=500,widget=forms.TextInput(attrs={'placeholder':'Ingresa el producto o servicio en el que estas interesado','class': 'input'}))