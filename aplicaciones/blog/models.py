from django.db import models
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Categoría', max_length =50)
    estado = models.BooleanField('Categoría Activada/Desactivada', default=True)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)
    fecha_edicion = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de autor', max_length=200)
    apellidos = models.CharField('Apellidos de autor', max_length=200)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo Eléctronico')
    estado = models.BooleanField('Autor Activada/Desactivada', default=True)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)
    fecha_edicion = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombres)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=90)
    slug = models.CharField('Slug', max_length=100)
    descripcion = models.CharField('Descripción', max_length=110)
    contenido = RichTextField()
    imagen = models.URLField('Imágen', max_length=300) #pq heroku no permite almacenar imágenes en su versión gratuita
    estado = models.BooleanField('Publicado Activo/Desactivo', default=True)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)
    fecha_edicion = models.DateTimeField('Fecha de edición', auto_now=True)
    #rel
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    
    

