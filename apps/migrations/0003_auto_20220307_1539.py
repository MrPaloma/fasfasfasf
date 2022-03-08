# Generated by Django 3.2 on 2022-03-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_member_person_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, help_text='Dirección', max_length=200, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, help_text='Número de Teléfono Fijo o de Oficina', max_length=10, null=True, verbose_name='Teléfono'),
        ),
    ]