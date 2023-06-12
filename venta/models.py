from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    rol = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"