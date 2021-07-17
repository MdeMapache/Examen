import re
from django.http import response
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Vehiculo
from .serializers import VehiculoSerializer
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_vehiculos(request):
    '''
    Lista todos los vehiculos
    '''
    if(request.method=='GET'):
        vehiculo=Vehiculo.objects.all()
        serializer=VehiculoSerializer(vehiculo, many=True)
        return Response(serializer.data)

    elif(request.method=='POST'):
        data=JSONParser().parse(request)
        serializer=VehiculoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_vehiculo(request,id):
    '''
    Get, update o delete de un vehiculo

    '''
    try: #verifivar patente ingresada existe
        vehiculo =Vehiculo.objects.get(patente=id)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method=='GET'): #recuperar 1 vehiculo por patente
        serializer=VehiculoSerializer(vehiculo)
        return Response(serializer.data)

    if(request.method=='PUT'):#actualizar 1 vehiculo por patente
        data=JSONParser().parse(request)
        serializer=VehiculoSerializer(vehiculo,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE'):#eliminar un vehiculo por patente
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
