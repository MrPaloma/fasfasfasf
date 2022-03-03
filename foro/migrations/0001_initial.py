# Generated by Django 3.2 on 2022-03-03 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('normas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories_foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Nombre de Categoria', max_length=200, verbose_name='Nombre de Categoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': '1. Foro Categorias',
            },
        ),
        migrations.CreateModel(
            name='Subcategories_foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(help_text='Subcategoria', max_length=200, verbose_name='Subcategoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.categories_foro')),
            ],
            options={
                'verbose_name_plural': '2. Foro SubCategorias',
            },
        ),
        migrations.CreateModel(
            name='Themas_foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themas_name', models.CharField(help_text='Nombre de Tema', max_length=200, verbose_name='Nombre de Tema')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.subcategories_foro')),
            ],
            options={
                'verbose_name_plural': '3. Foro Temas',
            },
        ),
        migrations.CreateModel(
            name='Coments_foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.CharField(help_text='comentario', max_length=200, verbose_name='comentario')),
                ('likes', models.PositiveSmallIntegerField(default=0, help_text='Likes', verbose_name='Likes')),
                ('dislikes', models.PositiveSmallIntegerField(default=0, help_text='Dislikes', verbose_name='Dislikes')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('tema', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='normas.register_normativa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
