from django.db import models

# Create your models here.

class Auto(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    anio=models.IntegerField()
    airbag=models.BooleanField()

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Perro(models.Model):
    nombre=models.CharField(max_length=30)
    raza=models.CharField(max_length=30)
    genero=models.CharField(max_length=6)
    edad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} | {self.raza}"

class Equipo(models.Model):
    pais=models.CharField(max_length=30)
    continente=models.CharField(max_length=30)
    sigueJugando=models.BooleanField()

    def __str__(self):
        return f"{self.pais}"