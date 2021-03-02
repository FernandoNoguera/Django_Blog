from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
                                    Q(titulo__icontains=queryset)|
                                    Q(descripcion__icontains=queryset),
                                    estado = True,
                                    categoria = Categoria.objects.get(nombre__iexact = 'General'),
                                    ).distinct()
    paginator = Paginator(posts,5) #para paginado se le pasa los elementos a paginar y la cantidad 
    page = request.GET.get('page') #guardamos la pagina actual en la que nos encontramos navegando en el template
    posts = paginator.get_page(page) #se vuelve a definir post para definir solo los post que se encuentran en la pagina indicada
    return render(request, 'index.html', {'posts':posts})


def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'General'))
    if queryset:
        posts = Post.objects.filter(
                                Q(titulo__icontains=queryset)|
                                Q(descripcion__icontains=queryset),
                                estado = True,
                                categoria = Categoria.objects.get(nombre__iexact = 'General'),
                                ).distinct()
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generales.html', {'posts':posts})


def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'Programación'))
    if queryset:
        posts = Post.objects.filter(
                                Q(titulo__icontains=queryset)|
                                Q(descripcion__icontains=queryset),
                                estado = True,
                                categoria = Categoria.objects.get(nombre__iexact = 'Programación'),
                                ).distinct()
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programacion.html', {'posts':posts})


def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'Tecnología'))
    if queryset:
        posts = Post.objects.filter(
                                Q(titulo__icontains=queryset)|
                                Q(descripcion__icontains=queryset),
                                estado = True,
                                categoria = Categoria.objects.get(nombre__iexact = 'Tecnología'),
                                ).distinct()
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnologia.html', {'posts':posts})


def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    if queryset:
        posts = Post.objects.filter(
                                Q(titulo__icontains=queryset)|
                                Q(descripcion__icontains=queryset),
                                estado = True,
                                categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'),
                                ).distinct()
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videojuegos.html', {'posts':posts})



def detallePost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'post.html', {'detalle_post':post})


