# Generated by Django 4.2 on 2024-05-23 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRANSACTION', '0017_alter_operaciones_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operaciones',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRANSACTION.subcategory'),
        ),
    ]