# Generated by Django 4.2 on 2024-07-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRANSACTION', '0030_operaciones_fecha_pago_operaciones_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operaciones',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
