from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_proyectos.views import CategoriaProyectoViewSet, ProyectoIntegradorViewSet, AñoViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaProyectoViewSet)
router.register(r'proyectos', ProyectoIntegradorViewSet)
router.register(r'años', AñoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
