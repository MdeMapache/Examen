import django
from django.shortcuts import render, redirect
from .models import Proveedores, Vehiculo
from .forms import ProveedorForm, VehiculoForm,CustomUserCreationForm,UserRegisterForm,ContactoForm,ProveedorForm
#para el registro
from django.contrib.auth.forms import UserCreationForm
#para login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


# Paso 1
def home(request):
    #return render(request,'core/home.html')
    vehiculos=Vehiculo.objects.all
    #creo la variable que le pase los datos del vehiculo al template
    datos={
        'vehiculos': vehiculos
    }
    return render(request,'core/home.html',datos)
@permission_required('core.view_vehiculo')
def index(request):
    #return render(request,'core/home.html')
    vehiculos=Vehiculo.objects.all
    #creo la variable que le pase los datos del vehiculo al template
    datos={
        'vehiculos': vehiculos
    }
    return render(request,'core/index.html',datos)

def galeria(request):
    vehiculos=Vehiculo.objects.all
    datos={
        'vehiculos': vehiculos
    }
    return render(request,'core/galeria.html', datos)

def contacto(request):
    data ={
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "contacto enviado"
        else:
            data["form"] = formulario

    return render(request, 'core/contacto.html',data)

    

def imagencarru(request):
    return render(request,'core/imagencarru.html')
    
def imagencarru2(request):
    return render(request,'core/imagencarru2.html')
    
def imagencarru3(request):
    return render(request,'core/imagencarru3.html')

def login(request):
    return render(request,'core/login.html')

def mecanica(request):
    return render(request,'core/mecanica.html')

def pintura(request):
    return render(request,'core/pintura.html')

def revision(request):
    return render(request,'core/revision.html')

def somos(request):
    return render(request,'core/somos.html')
@login_required
@permission_required('core.add_vehiculo')
def form_vehiculo(request):
    datos={'form' : VehiculoForm}
    if request.method=='POST':
        formulario=VehiculoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request, 'core/form_vehiculo.html', datos)

def addProveedor(request):
    datos={'form' : ProveedorForm}
    if request.method=='POST':
        formulario=ProveedorForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request, 'core/addProveedor.html', datos)
def listProveedor(request):
    #return render(request,'core/home.html')
    proveedor=Proveedores.objects.all
    #creo la variable que le pase los datos del vehiculo al template
    datos={
        'proveedor': proveedor
    }
    return render(request,'core/listProveedor.html',datos)

@login_required
@permission_required('core.change_vehiculo')
def form_mod_vehiculo(request,id):
    vehiculo=Vehiculo.objects.get(patente=id)
    datos={'form':VehiculoForm(instance=vehiculo)}
    if request.method=='POST':
        formulario=VehiculoForm(data=request.POST, instance=vehiculo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Modificado Correctamente"

    return render(request, 'core/form_mod_vehiculo.html', datos)
@login_required

def form_del_vehiculo(request,id):
    vehiculo=Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="index")

@permission_required('core.add_user')
def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
           
            #redirigir al home
            
            return redirect(to="home")
        data["form"] = formulario

    return render(request,'registration/registro.html', data)

def registroP(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} Creado')
            return render(request, 'core/home.html')
    else:
        form = UserRegisterForm()

    context  = {'form' : form}
    return render(request, 'registration/registroP.html', context)