# Generated by Django 3.2 on 2022-03-07 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20220307_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='suscribcion_foro',
        ),
    ]