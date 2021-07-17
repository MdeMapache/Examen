# Generated by Django 3.2.5 on 2021-07-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210717_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedores',
            name='NombreP',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre Compañia proveedora'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='NumeroIdentificador',
            field=models.IntegerField(verbose_name='Numero Identificador'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='Telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Avatar o logo'),
        ),
    ]
