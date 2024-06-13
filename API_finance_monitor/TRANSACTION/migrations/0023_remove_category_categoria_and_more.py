# Generated by Django 4.2 on 2024-06-01 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRANSACTION', '0022_alter_subcategory_multiplicador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='subcategoria',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operaciones',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TRANSACTION.category'),
        ),
        migrations.AlterField(
            model_name='operaciones',
            name='subcategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TRANSACTION.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='multiplicador',
            field=models.IntegerField(choices=[(1, '+'), (-1, '-')], default=1),
        ),
    ]