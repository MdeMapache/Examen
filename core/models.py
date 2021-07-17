from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.forms import widgets
from django.forms.widgets import PasswordInput
from django.core.validators import MaxValueValidator


# Create your models here.

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id Categoria')
    
    def __str__(self):
        return self.nombreCategoria

opciones_servicio =[
    [0,"mecanica"],
    [1,"desabolladuria y pintura"],
    [2, "revision tecnica"]


]
class Vehiculo(models.Model):
    patente=models.CharField(max_length=6,primary_key=True, verbose_name='Patente')
    marca=models.CharField(max_length=20,verbose_name='Marca del vehiculo')
    problema=models.TextField(max_length=50,verbose_name='Problema del Vehiculo')
    numero=models.IntegerField(verbose_name='Numero Cliente')
    servicio = models.IntegerField(choices=opciones_servicio)
    nombreC=models.CharField(max_length=30,verbose_name='Nombre del cliente', null=True)
    Categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True, verbose_name='Imagen')
    
 
    def __str__(self):
        return self.patente



opciones_consultas =[
    [0,"consulta"],
    [1,"reclamo"],
    [2, "suggerencia"],
    [3,"felicitaciones"]

]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    aviso = models.BooleanField()

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    NumeroIdentificador = models.IntegerField(verbose_name='Numero Identificador')
    NombreC=models.CharField(max_length=30,verbose_name='Nombre Completo', null=True)
    NombreP=models.CharField(max_length=30,verbose_name='Nombre Compañia proveedora', null=True)
    Direccion = models.CharField(max_length=50 ,verbose_name='Direccion')
    Telefono = models.IntegerField()
    email =models.EmailField()
    pais =models.CharField(max_length=20,verbose_name='Pais')
    imagen = models.ImageField(null=True, blank=True, verbose_name='Avatar o logo')

    def __str__(self):
        return self.NombreC
    
