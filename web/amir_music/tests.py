from django.test import TestCase
from amir_music.models import *

class DBTestCase(TestCase):
  def setUp(self) -> None:
    grupo = Grupo(nombre="Fondo Flamenco", fecha_fundacion=datetime(2006,6,18), estilo="flamenco").save()
    Album(grupo=grupo, titulo="Primer disco", ).save()
    return super().setUp()
  def test_models_can_be_accessed(self):
    grupo = Grupo.objects(nombre="Fondo Flamenco")
    album = Album.objects(titulo="Primer disco")
    self.assertEqual(grupo.first().nombre, "Fondo Flamenco")
    self.assertEqual(album.first().titulo, "Primer disco")
