from rest_framework import serializers
from .models import ProyectoIntegrador, CategoriaProyecto, Año, Grupo, Alumno, Seccion

class AñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Año
        fields = ['id', 'año', 'semestre']

class CategoriaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProyecto
        fields = ['id', 'nombre']


class ProyectoIntegradorSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True)
    categoria = CategoriaProyectoSerializer()
    año = AñoSerializer()

    class Meta:
        model = ProyectoIntegrador
        fields = [
            'id', 'titulo', 'descripcion', 'año', 'imagen', 'documento', 
            'video', 'url_github', 'categoria'
        ]

    def create(self, validated_data):
        # Extraer los datos anidados
        categoria_data = validated_data.pop('categoria')
        año_data = validated_data.pop('año')

        # Buscar o crear el año
        año_instance, created = Año.objects.get_or_create(
            año=año_data.get('año'),
            semestre=año_data.get('semestre')
        )

        # Buscar o crear la categoría
        categoria_instance, created = CategoriaProyecto.objects.get_or_create(
            nombre=categoria_data.get('nombre')
        )

        # Crear la instancia del Proyecto Integrador
        proyecto_integrador_instance = ProyectoIntegrador.objects.create(
            categoria=categoria_instance,
            año=año_instance,
            **validated_data
        )

        return proyecto_integrador_instance



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
    proyecto_nombre = serializers.CharField(source='proyecto.titulo', read_only=True)  

    class Meta:
        model = Alumno
        fields = ['id', 'nombre', 'apellido', 'grupo', 'seccion', 'proyecto', 'proyecto_nombre']

