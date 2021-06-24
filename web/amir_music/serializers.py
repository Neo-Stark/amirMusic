from .models import Album, Musico, Grupo
from rest_framework import serializers

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        
class MusicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musico
        fields = '__all__'

class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'