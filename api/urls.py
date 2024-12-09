from django.urls import path, include

urlpatterns = [
    # Incluir las rutas de la app 'api' (si contiene la configuración de las rutas para el token)
    path('api/', include('api.urls')),
]