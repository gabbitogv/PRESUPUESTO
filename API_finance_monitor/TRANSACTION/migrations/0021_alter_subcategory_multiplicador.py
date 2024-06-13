# Generated by Django 4.2 on 2024-05-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRANSACTION', '0020_subcategory_multiplicador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='multiplicador',
            field=models.IntegerField(choices=[(1, 1), (-1, -1)], default=1, max_length=2),
        ),
    ]
