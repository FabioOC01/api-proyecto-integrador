from django.http import JsonResponse
from django.shortcuts import render
from .models import ProyectoIntegrador

# Vista para la ruta /api/
def mi_vista_api(request):
    # Crear una respuesta JSON con un mensaje
    return JsonResponse({"message": "Bienvenido a la API"})

# Ejemplo de vista para obtener todos los proyectos integradores
def obtener_proyectos(request):
    proyectos = ProyectoIntegrador.objects.all().values('id', 'titulo', 'descripcion')
    return JsonResponse(list(proyectos), safe=False)

# Ejemplo de vista para obtener un proyecto específico por ID
def obtener_proyecto(request, proyecto_id):
    try:
        proyecto = ProyectoIntegrador.objects.get(id=proyecto_id)
        data = {
            'id': proyecto.id,
            'titulo': proyecto.titulo,
            'descripcion': proyecto.descripcion
        }
        return JsonResponse(data)
    except ProyectoIntegrador.DoesNotExist:
        return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)

