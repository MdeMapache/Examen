from django.urls import path
from .views import home,contacto,galeria,imagencarru,imagencarru2,imagencarru3,login,mecanica,pintura,revision,somos,form_mod_vehiculo,form_vehiculo,index,form_del_vehiculo,login,registro,registroP,addProveedor,listProveedor

#paso 2
urlpatterns=[
    path('',home,name="home"),
    path('datos',index,name="index"),
    path('contactoc',contacto,name="contacto"),
    path('galeriag',galeria,name="galeria"),
    path('imagencarrui',imagencarru,name="imagencarru"),
    path('imagencarrui2',imagencarru2,name="imagencarru2"),
    path('imagencarrui3',imagencarru3,name="imagencarru3"),
    path('loginl',login,name="login"),
    path('mecanicam',mecanica,name="mecanica"),
    path('pinturap',pintura,name="pintura"),
    path('revisionr',revision,name="revision"),
    path('somoss',somos,name="somos"),
    path('form-vehiculo', form_vehiculo,name="form_vehiculo"),
    path('form-mod-vehiculo/<id>', form_mod_vehiculo,name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>', form_del_vehiculo,name="form_del_vehiculo"),
    path('registro',registro,name="registro"),
    path('registroP',registroP,name="registroP"),
    path('addProveedor',addProveedor,name="addProveedor"),
    path('listProveedor',listProveedor,name="listProveedor")
   
    
    

]