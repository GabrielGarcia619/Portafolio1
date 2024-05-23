from django.db import models

# Create your models here.
class PerfilProfecional (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)