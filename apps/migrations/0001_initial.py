# Generated by Django 3.2 on 2022-04-19 17:08

import apps.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foro', '0001_initial'),
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_surname', models.CharField(blank=True, help_text='Apellido Paterno', max_length=50, verbose_name='Apellido Paterno')),
                ('second_surname', models.CharField(blank=True, help_text='Apellido Materno', max_length=50, verbose_name='Apellido Materno')),
                ('names', models.CharField(help_text='Nombres O Razón Social', max_length=50, verbose_name='Nombres')),
                ('full_name', models.CharField(default='Nombre completo', help_text='Apellidos y Nombres', max_length=200, verbose_name='Apellidos y Nombres')),
                ('person_type', models.CharField(blank=True, choices=[('N', 'NATURAL'), ('J', 'JURÍDICA')], default='N', help_text='Tipo de Persona', max_length=1, verbose_name='Tipo de Persona')),
                ('identity', models.CharField(blank=True, help_text='DNI o RUC', max_length=11, verbose_name='Documento de Identidad')),
                ('profession', models.CharField(blank=True, choices=[('A', 'ARQUITECTO'), ('I', 'INGENIERO'), ('O', 'OTRO')], help_text='Profesión', max_length=1, verbose_name='Profesión')),
                ('mobile', models.CharField(blank=True, help_text='Número de Teléfono Celular', max_length=12, verbose_name='Celular')),
                ('phone', models.CharField(blank=True, help_text='Número de Teléfono Fijo o de Oficina', max_length=10, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(help_text='Correo Electrónico', max_length=50, verbose_name='Email')),
                ('tuition', models.PositiveIntegerField(blank=True, help_text='Colegiatura', null=True, verbose_name='Colegiatura')),
                ('secret_code', models.PositiveIntegerField(blank=True, help_text='Código Secreto de Arquitecto', null=True, verbose_name='Código Secreto de Arquitecto')),
                ('address', models.CharField(blank=True, help_text='Dirección', max_length=200, null=True, verbose_name='Dirección')),
                ('area_interest', models.CharField(blank=True, help_text='areas de interes', max_length=200, verbose_name='areas de interes')),
                ('institution', models.CharField(blank=True, help_text='Institucion', max_length=200, verbose_name='Institucion')),
                ('photo', models.ImageField(blank=True, help_text='Suba una fotografía en tamaño pasaporte o carnet', null=True, upload_to=apps.models.upload_photos, verbose_name='Fotografía')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('is_enabled', models.BooleanField(default=False, verbose_name='¿Esta habilitado?')),
                ('penalty_fee', models.BooleanField(default=False, verbose_name='¿Tiene multas?')),
                ('has_tutition', models.BooleanField(default=False, verbose_name='¿Es colegiado?')),
                ('is_client', models.BooleanField(default=False, verbose_name='¿Es cliente?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_membership', to='membership.membership')),
                ('suscripcion_foro', models.ManyToManyField(blank=True, related_name='suscripcion_foro', to='foro.Foro')),
                ('user', models.OneToOneField(blank=True, help_text='Usuario', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_membership', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Relacion de Miembros',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planame', models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Plan')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Planes de Suscripcion',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_profile', models.OneToOneField(help_text='Usuario', on_delete=django.db.models.deletion.CASCADE, to='apps.member', verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.CreateModel(
            name='UsagePolicies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(verbose_name='Politicas de uso')),
                ('validity_date_start', models.DateField(help_text='Fecha Inicio', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha Fin', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('member_policies', models.ManyToManyField(blank=True, related_name='member_policies', to='apps.Member')),
            ],
            options={
                'verbose_name': 'Politicas de Uso',
                'verbose_name_plural': 'Politicas de Uso',
            },
        ),
        migrations.CreateModel(
            name='Order_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(blank=True, help_text='Nombres O Razón Social', max_length=50, verbose_name='Nombres')),
                ('first_surname', models.CharField(blank=True, help_text='Apellido Paterno', max_length=50, verbose_name='Apellido Paterno')),
                ('second_surname', models.CharField(blank=True, help_text='Apellido Materno', max_length=50, verbose_name='Apellido Materno')),
                ('email', models.EmailField(blank=True, help_text='Correo Electrónico', max_length=50, null=True, verbose_name='Email')),
                ('identity', models.CharField(blank=True, help_text='DNI o RUC', max_length=11, verbose_name='Documento de Identidad')),
                ('paid', models.BooleanField(default=False)),
                ('niubiz_id', models.CharField(blank=True, max_length=150)),
                ('pay_method', models.CharField(blank=True, choices=[('E', 'VISA'), ('V', 'EFECTIVO')], help_text='Metodo de Pago', max_length=1, verbose_name='Metodo de Pago')),
                ('pay_import', models.DecimalField(decimal_places=2, help_text='Importe Pagado', max_digits=10, verbose_name='Importe Pagado')),
                ('validity_date_start', models.DateTimeField(help_text='Fecha Inicio membresia', verbose_name='Fecha Inicio membresia')),
                ('validity_date_finish', models.DateTimeField(help_text='Fecha Fin membresia', verbose_name='Fecha Fin membresia')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificacion del Registro', verbose_name='Fecha de Modificacion del Registro')),
                ('member', models.ForeignKey(blank=True, help_text='Miembros', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_order', to='apps.member', verbose_name='Miembros')),
            ],
            options={
                'verbose_name': 'Ordenes de Pagos',
                'verbose_name_plural': 'Ordenes de Pagos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NiubizTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecoreTransactionUUID', models.CharField(blank=True, max_length=100, verbose_name='Identificador de la transaccion niubiz')),
                ('channel', models.CharField(blank=True, max_length=100, verbose_name='Canal de registro')),
                ('signature', models.CharField(blank=True, max_length=100, verbose_name='Codigo niubiz')),
                ('tokenId', models.CharField(blank=True, max_length=100, verbose_name='Token formulario niubiz')),
                ('purchaseNumber', models.CharField(blank=True, max_length=100, verbose_name='Numero de pedido')),
                ('amount', models.CharField(blank=True, max_length=100, verbose_name='Importe de la transaccion')),
                ('installment', models.CharField(blank=True, max_length=100, verbose_name='Numero de cuotas')),
                ('currency', models.CharField(blank=True, max_length=100, verbose_name='Moneda')),
                ('authorizedAmount', models.CharField(blank=True, max_length=100, verbose_name='Importe confirmado')),
                ('authorizationCode', models.CharField(blank=True, max_length=100, verbose_name='Codigo de autorización')),
                ('traceNumber', models.CharField(blank=True, max_length=100, verbose_name='Identificador de la orden de transaccion')),
                ('card', models.CharField(blank=True, max_length=16, verbose_name='Numero de tarjeta')),
                ('action_description', models.CharField(blank=True, max_length=100, verbose_name='Descripcion de la transaccion')),
                ('brand', models.CharField(blank=True, max_length=15, verbose_name='Nombre de la tarjeta')),
                ('order_pyment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='niubiz_transaction', to='apps.order_payment')),
            ],
            options={
                'verbose_name': 'Transaccion Niubiz',
                'verbose_name_plural': 'Transaccion Niubiz',
            },
        ),
    ]
