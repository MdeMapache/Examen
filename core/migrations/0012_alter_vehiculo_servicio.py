# Generated by Django 3.2.5 on 2021-07-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_vehiculo_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='servicio',
            field=models.IntegerField(choices=[[0, 'mecanica'], [1, 'desabolladuria y pintura'], [2, 'revision tecnica']]),
        ),
    ]