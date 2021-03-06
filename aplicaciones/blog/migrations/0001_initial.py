# Generated by Django 3.1.7 on 2021-02-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres de autor')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos de autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Eléctronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor Activada/Desactivada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_edicion', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de Categoría')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoría Activada/Desactivada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_edicion', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
    ]
