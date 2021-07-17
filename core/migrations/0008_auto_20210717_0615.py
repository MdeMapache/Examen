# Generated by Django 3.2.5 on 2021-07-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210717_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'suggerencia'], [3, 'felicitaciones']])),
                ('mensaje', models.TextField()),
                ('aviso', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='numero',
            field=models.IntegerField(verbose_name='Numero Cliente'),
        ),
    ]
