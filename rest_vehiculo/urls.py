from django.urls import path
from django.urls.resolvers import URLPattern
from rest_vehiculo.views import lista_vehiculos, detalle_vehiculo

urlpatterns=[
    path('lista_vehiculos',lista_vehiculos, name="lista_vehiculos"),
    path('detalle_vehiculo/<id>', detalle_vehiculo, name="detalle_vehiculo"),

]