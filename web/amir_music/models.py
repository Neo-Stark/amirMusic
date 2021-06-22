from django.db import models

class Grupo(models.Model):
  nombre = models.CharField(max_length=200)
  fecha_fundacion = models.DateField()
  estilo = models.CharField(max_length=200)

  class Meta:
    ordering = ['-fecha_fundacion', 'nombre']

  def __str__(self):
    return self.nombre


class Musico(models.Model):
  grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE, null=True, blank=True)
  nombre = models.CharField(max_length=200)
  fecha_nacimiento = models.DateField(null=True)
  instrumento = models.CharField(max_length=200, null=True)
  lon = models.FloatField(null=True, blank=True)
  lat = models.FloatField(null=True, blank=True)

  class Meta:
    ordering = ['grupo', 'nombre']


  def __str__(self):
    return self.nombre

class Album(models.Model):
  grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)
  titulo = models.CharField(max_length=200)
  cover = models.ImageField(upload_to='images/', null=True)
  fecha_lanzamiento = models.DateField(null=True, blank=True)
  distribuidora = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.titulo