# Generated by Django 3.2 on 2022-02-24 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('normas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategories_normas',
            options={'verbose_name_plural': '2.Normas - Subtipo De Normativa'},
        ),
        migrations.AlterModelOptions(
            name='subnormativa',
            options={'verbose_name_plural': '5.Normas-Normativa'},
        ),
        migrations.RemoveField(
            model_name='register_palabraclave',
            name='normativa',
        ),
        migrations.AddField(
            model_name='areas_normas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='areas_normas',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='categories_normas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='categories_normas',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='location_normas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='location_normas',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='master_normas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='master_normas',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='es_foro',
            field=models.BooleanField(default=False, verbose_name='Es un foro'),
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='es_vigente',
            field=models.BooleanField(default=False, verbose_name='Esta vigente'),
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='register_palabraclave',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='register_palabraclave',
            name='normativas',
            field=models.ManyToManyField(related_name='keywords', to='normas.Register_Normativa', verbose_name='Normativa'),
        ),
        migrations.AddField(
            model_name='register_palabraclave',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='subcategories_normas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='subcategories_normas',
            name='order',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='subcategories_normas',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='subnormativa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='subnormativa',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='register_normativa',
            name='document',
            field=models.FileField(null=True, upload_to='Document_normativa', verbose_name='Documentos'),
        ),
        migrations.AlterField(
            model_name='register_normativa',
            name='tipo_norma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.subcategories_normas', verbose_name='Tipo de Norma'),
        ),
        migrations.AlterField(
            model_name='register_normativa',
            name='tipo_uso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.areas_normas', verbose_name='Tipo Uso'),
        ),
        migrations.AlterField(
            model_name='register_palabraclave',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nombre Palabra Clave'),
        ),
        migrations.AlterField(
            model_name='subnormativa',
            name='norma',
            field=models.CharField(max_length=200, verbose_name='Normativa'),
        ),
        migrations.AlterField(
            model_name='subnormativa',
            name='norma_sub',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='normas.subcategories_normas', verbose_name='Sub Normativa'),
        ),
    ]
