
from django import urls
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'grupo',views.GrupoViewSet)
router.register(r'musico',views.MusicoViewSet)
router.register(r'album',views.AlbumViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^album/detalles/(?P<oid>[0-9]+)/$', views.detalles_album, name='detalles_album'),
    url(r'^grupos/form', views.form_grupo, name='form_grupo'),
    url(r'^album/form', views.form_album, name='form_album'),
    url(r'^musicos/form', views.form_musico, name='form_musico'),
    url(r'^modificar/(?P<model>\w+)/(?P<oid>[0-9]+)/$', views.modificar, name='modificar'),
    url(r'^eliminar/(?P<model>\w+)/(?P<oid>[0-9]+)/$', views.eliminar, name='eliminar'),
    url(r'^mapa/$', views.mapa, name='mapa'),
    url(r'^graficos/$', views.graficos, name='graficos'),
    url(r'^get_posicion_musicos/$', views.get_posicion_musicos, name='get_posicion_musicos'),
    url(r'^get_grupos_musicos/$', views.get_grupos_musicos, name='get_grupos_musicos'),
    url(r'^get_musicos_year/$', views.get_musicos_year, name='get_musicos_year'),
]
