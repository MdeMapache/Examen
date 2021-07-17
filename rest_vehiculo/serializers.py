from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from core.models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehiculo
        fields=["nombreC","numero","patente","marca","problema"]