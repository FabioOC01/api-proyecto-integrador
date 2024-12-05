from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProyectoIntegradorViewSet, CategoriaProyectoViewSet, AñoViewSet, GrupoViewSet, AlumnoViewSet, SeccionViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'proyectos', ProyectoIntegradorViewSet)
router.register(r'categorias', CategoriaProyectoViewSet)
router.register(r'anos', AñoViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'secciones', SeccionViewSet)  

urlpatterns = [
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 