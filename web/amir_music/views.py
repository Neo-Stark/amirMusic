from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from django.template.loader import render_to_string
from rest_framework import viewsets

from .forms import *
from .models import *
from .serializers import *

# API views

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    
class MusicoViewSet(viewsets.ModelViewSet):
    queryset = Musico.objects.all()
    serializer_class = MusicoSerializer

# End/ API views

def render_form(request, class_form):
    if 'cover' in request.FILES:
        print(request.FILES['cover'])
    if request.method == 'POST':
        form = class_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/amirMusic")
    else:
        form = class_form()

    return render(request, 'formulario_base.html', {'form': form,
                                                    'nombre': form.Meta.model.__name__,
                                                    'tipo': 'Nuevo'})


def form_grupo(request):
    return render_form(request, GrupoForm)


def form_album(request):
    return render_form(request, AlbumForm)


def form_musico(request):
    return render_form(request, MusicoForm)


def index(request):
    if request.GET.get('busqueda'):
        musicos_list = Musico.objects.filter(nombre__icontains=request.GET.get('busqueda'))
        grupos_list = Grupo.objects.filter(nombre__icontains=request.GET.get('busqueda'))
        albumes = Album.objects.filter(titulo__icontains=request.GET.get('busqueda'))
    else:    
        musicos_list = Musico.objects.all()
        grupos_list = Grupo.objects.all()
        albumes = Album.objects.all()

    paginator = Paginator(grupos_list, 5)
    page = request.GET.get('pageGrupos')
    grupos = paginator.get_page(page)

    if (request.is_ajax()):
        return JsonResponse(render_to_string('grupos.html', {'grupos': grupos}), safe=False)

    paginator = Paginator(musicos_list, 5)
    page = request.GET.get("page")
    musicos = paginator.get_page(page)

    return render(request, 'index.html', {'musicos': musicos, 'grupos': grupos, 'albumes': albumes})


def modificar(request, model, oid):
    switcher = {
        "Musico": Musico,
        "Grupo": Grupo,
        "Album": Album
    }
    switcherForm = {
        "Musico": MusicoForm,
        "Grupo": GrupoForm,
        "Album": AlbumForm
    }
    form = switcherForm.get(model)
    object = switcher.get(model).objects.filter(id=oid).first()
    if request.method == "POST":
        form = form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = form(instance=object)
    return render(request, 'formulario_base.html', {'form': form,
                                                    'nombre': form.Meta.model.__name__,
                                                    'tipo': 'Modificar'})


def eliminar(request, model, oid):
    switcher = {
        "Musico": Musico,
        "Grupo": Grupo,
        "Album": Album
    }
    switcher.get(model).objects.filter(id=oid).delete()
    return redirect('index')

def detalles_album(request, oid):
    album = Album.objects.filter(id=oid).first()
    return render(request, 'detalles_album.html', {'album': album})


def mapa(request):
    return render(request, 'mapa.html')


def graficos(request):
    return render(request, 'graficos.html')


def get_posicion_musicos(request):
    posicion = list(Musico.objects.exclude(
        lon__isnull=True).values('lon', 'lat', 'nombre'))
    print(posicion)
    return JsonResponse(posicion, safe=False)


def get_grupos_musicos(request):
    grupos = list(Musico.objects.exclude(grupo__isnull=True).values(
        'grupo__nombre').annotate(Count('grupo')))
    grupos.append({
        'grupo__nombre': "Sin grupo",
        'grupo__count': Musico.objects.filter(grupo__isnull=True).count()
    })
    return JsonResponse(grupos, safe=False)


def get_musicos_year(request):
    years = list(Musico.objects.values('fecha_nacimiento__year').annotate(
        Count('fecha_nacimiento__year')))
    print(years)
    return JsonResponse(years, safe=False)
