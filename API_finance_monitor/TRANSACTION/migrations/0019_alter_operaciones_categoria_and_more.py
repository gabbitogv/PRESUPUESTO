# Generated by Django 4.2 on 2024-05-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRANSACTION', '0018_alter_operaciones_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operaciones',
            name='categoria',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='operaciones',
            name='subcategoria',
            field=models.CharField(max_length=250),
        ),
    ]