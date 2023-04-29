from django.db import models

class Turno(models.Model):

    fecha = models.DateField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    vehiculo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.fecha} - {self.telefono} - {self.vehiculo} - {self.comentario}'    