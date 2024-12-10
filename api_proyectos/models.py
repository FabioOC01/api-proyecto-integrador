from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError

class CategoriaProyecto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Año(models.Model):
    año = models.IntegerField(default=date.today().year)

    def __str__(self):
        return f"{self.año}"

    class Meta:
        pass # No necesitas unique_together


class ProyectoIntegrador(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    año = models.ForeignKey(Año, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    documento = models.FileField(upload_to='documentos/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    url_github = models.URLField(max_length=255, null=True, blank=True)
    categoria = models.ForeignKey(CategoriaProyecto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Seccion(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, null=True, blank=True)
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'api_proyectos_alumno'  # Especificamos el nombre deseado para la tabla

class AlumnoProyecto(models.Model):
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, null=True, blank=True)
    año = models.ForeignKey(Año, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('proyecto', 'grupo')

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE, null=True, blank=True)

class HistorialProyecto(models.Model):
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=255, default="")
    descripcion = models.TextField(default="")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=1)

class Valoracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    proyecto = models.ForeignKey(ProyectoIntegrador, on_delete=models.CASCADE, null=True, blank=True)
    estrellas = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
