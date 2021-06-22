from datetime import datetime

from mongoengine import Document, EmbeddedDocument
from mongoengine.connection import connect
from mongoengine.fields import (DateTimeField, EmbeddedDocumentField,
                                FloatField, ListField, ReferenceField,
                                StringField)

connect(host="mongo", db="amir_music")

class Comentarios(EmbeddedDocument):
	contenido = StringField(required=True)
	autor     = StringField(max_length=120, required=True)
	fecha     = DateTimeField(default=datetime.now())

class Grupo(Document):
  nombre = StringField(primary_key=True, max_length=200)
  fecha_fundacion = DateTimeField()
  estilo = StringField(max_length=200)

  def __str__(self):
    return self.nombre

class Musico(Document):
  grupo = ReferenceField('Grupo')
  nombre = StringField(primary_key=True, max_length=200)
  fecha_nacimiento = DateTimeField(null=True)
  instrumento = StringField(max_length=200, null=True)
  lon = FloatField(null=True, blank=True)
  lat = FloatField(null=True, blank=True)
  
  def __str__(self):
    return self.nombre

class Album(Document):
  grupo = ReferenceField('Grupo')
  titulo = StringField(primary_key=True, max_length=200)
  fecha_lanzamiento = DateTimeField(null=True)
  distribuidora = StringField(max_length=200, null=True)
  comentarios = ListField(EmbeddedDocumentField(Comentarios), null=True)

  def __str__(self):
    return self.titulo

grupo = Grupo(nombre="Fondo Flamenco", fecha_fundacion=datetime(2006,6,18), estilo="flamenco")
album = Album(grupo=grupo, titulo="Primer disco", )
grupo.save()
album.save()

for grupo in Grupo.objects():
  print(grupo)

for album in Album.objects():
  print(album)
