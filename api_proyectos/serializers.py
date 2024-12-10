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
    # Usamos los serializers anidados en lugar de solo los IDs
    categoria = CategoriaProyectoSerializer()
    año = AñoSerializer()

    class Meta:
        model = ProyectoIntegrador
        fields = [
            'id', 'titulo', 'descripcion', 'año', 'imagen', 'documento', 
            'video', 'url_github', 'categoria'
        ]

    def create(self, validated_data):
        # Extraer los datos para los campos anidados
        categoria_data = validated_data.pop('categoria')
        año_data = validated_data.pop('año')

        # Crear las instancias de los modelos anidados
        categoria_instance = CategoriaProyecto.objects.create(**categoria_data)
        año_instance = Año.objects.create(**año_data)

        # Crear la instancia del ProyectoIntegrador con los objetos anidados
        proyecto_integrador_instance = ProyectoIntegrador.objects.create(
            categoria=categoria_instance,
            año=año_instance,
            **validated_data
        )

        return proyecto_integrador_instance

    def update(self, instance, validated_data):
        # Extraer los datos para los campos anidados
        categoria_data = validated_data.pop('categoria', None)
        año_data = validated_data.pop('año', None)

        # Actualizar las instancias de los modelos anidados si se pasan datos nuevos
        if categoria_data:
            for attr, value in categoria_data.items():
                setattr(instance.categoria, attr, value)
            instance.categoria.save()

        if año_data:
            for attr, value in año_data.items():
                setattr(instance.año, attr, value)
            instance.año.save()

        # Actualizar el ProyectoIntegrador
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

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

