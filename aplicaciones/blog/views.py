from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404


def home(request):
    posts = Post.objects.filter(estado = True)
    return render(request, 'index.html', {'posts':posts})


def generales(request):
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'General'))
    return render(request, 'generales.html', {'posts':posts})


def programacion(request):
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'Programación'))
    return render(request, 'programacion.html', {'posts':posts})


def tecnologia(request):
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'Tecnología'))
    return render(request, 'tecnologia.html', {'posts':posts})


def videojuegos(request):
    posts = Post.objects.filter(estado = True,categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    return render(request, 'videojuegos.html', {'posts':posts})



def detallePost(request,slug):

    post = get_object_or_404(Post,slug=slug)
    return render(request, 'post.html', {'detalle_post':post})


