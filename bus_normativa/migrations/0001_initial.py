# Generated by Django 3.2 on 2022-03-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='date_normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('subtitle', models.TextField(max_length=150, verbose_name='Subtitulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name_plural': 'Busqueda Normativas',
                'db_table': 'busqueda_normativa',
            },
        ),
    ]
