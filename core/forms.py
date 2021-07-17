from django import forms
from django.contrib.auth import models
from django.core.files.uploadhandler import UploadFileException
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import fields
from django.forms.fields import ImageField

from .models import Proveedores, Vehiculo, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#crear nuestra clasee para el formulario desde la bd
#recordar agragar mas datos
class VehiculoForm(ModelForm):
    nombreC = forms.CharField(min_length=5,required=True)
    numero = forms.IntegerField(min_value=1, max_value=9999999,required=True)
    patente = forms.CharField(min_length=4, max_length=4, required=True)
    problema = forms.CharField(min_length=5,max_length=50, required=True)
    nombreC = forms.CharField(required=True, min_length=3)
    marca = forms.CharField(required=True, min_length=3)
    patente = forms.CharField(required=True, min_length=6)
    
    
    
    
    
    

    class Meta:
        model=Vehiculo
        fields=["nombreC","numero","patente","marca","problema","Categoria","imagen","servicio"]

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True, min_length=5)
    class Meta:
        model = User
        fields =['username',"first_name","first_name","email","password1","password2","groups"]
        help_texts = {k:"" for k in fields}

class ProveedorForm(ModelForm):
    class Meta:
        model= Proveedores
        fields='__all__'

class UserRegisterForm(UserCreationForm):
    NumeroIdentificacion= forms.IntegerField(min_value=100, max_value=999)
    email = forms.EmailField(required=True, min_length=5)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    pais = forms.CharField(min_length=3)
    email = forms.EmailField(min_length=3)
    direccion = forms.CharField(min_length=5)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']
        help_texts = {k:"" for k in fields}


class ContactoForm(forms.ModelForm):
    nombre=forms.CharField(min_length=5,required=True)
    correo=forms.EmailField(min_length=4,required=True)
    mensaje=forms.CharField(required=False)
    class Meta:
        model = Contacto
        fields = '__all__'