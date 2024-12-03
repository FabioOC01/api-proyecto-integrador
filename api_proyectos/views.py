from rest_framework import viewsets
from .models import ProyectoIntegrador, CategoriaProyecto, Año, Grupo, Alumno
from .serializers import ProyectoIntegradorSerializer, CategoriaProyectoSerializer, AñoSerializer, GrupoSerializer, AlumnoSerializer

class ProyectoIntegradorViewSet(viewsets.ModelViewSet):
    queryset = ProyectoIntegrador.objects.all()
    serializer_class = ProyectoIntegradorSerializer

class CategoriaProyectoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProyecto.objects.all()
    serializer_class = CategoriaProyectoSerializer

class AñoViewSet(viewsets.ModelViewSet):
    queryset = Año.objects.all()
    serializer_class = AñoSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
