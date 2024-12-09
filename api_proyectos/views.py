from rest_framework import viewsets, generics
from .models import ProyectoIntegrador, CategoriaProyecto, Seccion, Año, Grupo, Alumno
from .serializers import ProyectoIntegradorSerializer, CategoriaProyectoSerializer, AñoSerializer, GrupoSerializer, AlumnoSerializer, SeccionSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "Debe proporcionar un nombre de usuario y contraseña"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "El nombre de usuario ya está en uso"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "Usuario creado exitosamente", "username": user.username})


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['user'] = {
            'username': request.user.username,
            'email': request.user.email,
        }
        return response
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected route.'})
    


class ProyectoIntegradorViewSet(viewsets.ModelViewSet):
    queryset = ProyectoIntegrador.objects.select_related('año', 'categoria').all()
    serializer_class = ProyectoIntegradorSerializer
    parser_classes = (MultiPartParser, FormParser) 

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


