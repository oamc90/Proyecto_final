from django.db import models

# Create your models here.

class Ingenieros(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50)
    proyecto=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    ingenieroACargo=models.CharField(max_length=50)
    estatus=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre +", Estado:" + self.estatus


class inventario_Tools(models.Model):
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    ubicacion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre