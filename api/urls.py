from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path

urlpatterns = [
    # Otras rutas
    path('auth/', include('api.urls')),  # Cambia "your_app_name" por el nombre de tu app
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 