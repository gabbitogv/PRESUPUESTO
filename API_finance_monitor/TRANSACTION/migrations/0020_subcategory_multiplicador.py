# Generated by Django 4.2 on 2024-05-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRANSACTION', '0019_alter_operaciones_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='multiplicador',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=1),
        ),
    ]