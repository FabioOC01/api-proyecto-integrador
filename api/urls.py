from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api_proyectos.views import ProyectoIntegradorViewSet, CategoriaProyectoViewSet, AñoViewSet, GrupoViewSet, AlumnoViewSet, SeccionViewSet
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
    path('api/', include(router.urls)),  # Rutas del router
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
