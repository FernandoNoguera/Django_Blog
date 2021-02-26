from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        models = Categoria


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre'] # para activar la barra de busqueda dentro del adminstrador
    list_display = ('id','nombre','estado', 'fecha_creacion') # para visualizar los diferentes campos en el encabezado de la tabla del admin
    resources_class = CategoriaResource


class AutorResource(resources.ModelResource):
    class Meta:
        models = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos']
    list_display = ('id','nombres','apellidos','correo','estado', 'fecha_creacion')
    resources_class = AutorResource



admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
