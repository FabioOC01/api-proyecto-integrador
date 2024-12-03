from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categorias', CategoriaProyectoViewSet)
router.register(r'proyectos', ProyectoIntegradorViewSet)
router.register(r'anios', AñoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
