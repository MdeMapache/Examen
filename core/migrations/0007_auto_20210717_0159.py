# Generated by Django 3.2.5 on 2021-07-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_vehiculo_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='correo',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='numero',
            field=models.IntegerField(max_length=9, verbose_name='Numero Cliente'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='problema',
            field=models.CharField(max_length=50, verbose_name='Problema del Vehiculo'),
        ),
    ]
