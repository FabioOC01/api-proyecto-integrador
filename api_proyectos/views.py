from rest_framework import viewsets, generics
from .models import ProyectoIntegrador, CategoriaProyecto, Seccion, Año, Grupo, Alumno
from .serializers import ProyectoIntegradorSerializer, CategoriaProyectoSerializer, AñoSerializer, GrupoSerializer, AlumnoSerializer, SeccionSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ProyectoIntegradorViewSet(viewsets.ModelViewSet):
    queryset = ProyectoIntegrador.objects.select_related('año', 'categoria').all()
    serializer_class = ProyectoIntegradorSerializer
    parser_classes = (MultiPartParser, FormParser)  # Permite recibir archivos

    def perform_update(self, serializer):
      serializer.save()
    
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
    queryset = Alumno.objects.select_related('grupo', 'seccion', 'proyecto').all()
    serializer_class = AlumnoSerializer

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer


