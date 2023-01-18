from django.db import models
from django.utils import timezone

class Empleados(models.Model):
    Num_Emp = models.IntegerField(default=0)
    Nombre = models.CharField(max_length=50, default="Escriba su nombre")
    Apellido = models.CharField(max_length=50, default="Escriba su apellido")
    Gen = (
        ("Hombre", "Hombre"),
        ("Mujer", "Mujer"),
        ("Desconocido", "Sin respuesta"),
        ("Otro", "Otro"),
    )
    Genero = models.CharField(max_length=20, choices=Gen, default='O')
    Fecha_Registro = models.DateField(blank=True, default=timezone.now)

