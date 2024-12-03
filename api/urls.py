from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/', views, name='api'),
    path('api/', views.mi_vista_api, name='mi_vista_api'),
    path('api/proyectos/', views.obtener_proyectos, name='obtener_proyectos'),
    path('api/proyectos/<int:proyecto_id>/', views.obtener_proyecto, name='obtener_proyecto'),
]
