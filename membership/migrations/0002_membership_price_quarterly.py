# Generated by Django 3.2 on 2022-03-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='price_quarterly',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Trimestral'),
        ),
    ]
