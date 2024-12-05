from rest_framework import serializers
from .models import ProyectoIntegrador, CategoriaProyecto, Año, Grupo, Alumno, Seccion

class AñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Año
        fields = ['id', 'año', 'semestre']

class CategoriaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProyecto
        fields = ['id', 'nombre', 'descripcion']


class ProyectoIntegradorSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True)
    documento = serializers.FileField(use_url=True)
    video = serializers.FileField(use_url=True)
    año = AñoSerializer()
    categoria = CategoriaProyectoSerializer()

    class Meta:
        model = ProyectoIntegrador
        fields = ['id', 'titulo', 'descripcion', 'año', 'imagen', 'documento', 'video', 'url_github', 'categoria']

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    seccion = SeccionSerializer(read_only=True)
    seccion_id = serializers.PrimaryKeyRelatedField(
        queryset=Seccion.objects.all(),
        source='seccion',
        write_only=True
    )

    class Meta:
        model = Grupo
        fields = ['id', 'nombre', 'seccion', 'seccion_id']

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id', 'nombre', 'apellido', 'grupo', 'seccion', 'año']


