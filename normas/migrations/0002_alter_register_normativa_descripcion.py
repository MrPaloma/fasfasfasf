# Generated by Django 3.2 on 2022-04-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_normativa',
            name='descripcion',
            field=models.CharField(blank=True, max_length=700, null=True, verbose_name='Descripcion'),
        ),
    ]
