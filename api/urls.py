from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_proyectos.views import ProyectoIntegradorViewSet, CategoriaProyectoViewSet, AñoViewSet, GrupoViewSet, AlumnoViewSet

router = DefaultRouter()
router.register(r'proyectos', ProyectoIntegradorViewSet)
router.register(r'categorias', CategoriaProyectoViewSet)
router.register(r'anos', AñoViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
