# Generated by Django 3.2.5 on 2021-07-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vehiculo_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='automoviles'),
        ),
    ]
