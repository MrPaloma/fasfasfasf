# Generated by Django 3.2 on 2022-03-20 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0017_remove_niubiztransaction_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niubiztransaction',
            name='order_pyment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='niubiz_transaction', to='apps.order_payment'),
        ),
    ]
