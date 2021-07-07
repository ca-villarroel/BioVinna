from rest_framework import serializers
from.models import Marcabio

class MarcabioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcabio
        fields = ['idMarca', 'nombre']
        
