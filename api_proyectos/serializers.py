from rest_framework import serializers
from .models import *

class CategoriaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProyecto
        fields = '__all__'

class ProyectoIntegradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoIntegrador
        fields = '__all__'

class AñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Año
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
