from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class CategoriaProyectoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProyecto.objects.all()
    serializer_class = CategoriaProyectoSerializer

class ProyectoIntegradorViewSet(viewsets.ModelViewSet):
    queryset = ProyectoIntegrador.objects.all()
    serializer_class = ProyectoIntegradorSerializer

class AñoViewSet(viewsets.ModelViewSet):
    queryset = Año.objects.all()
    serializer_class = AñoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
