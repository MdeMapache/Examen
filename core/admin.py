from django.contrib import admin
from .models import Categoria, Proveedores, Vehiculo, Contacto


admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Contacto)
admin.site.register(Proveedores)