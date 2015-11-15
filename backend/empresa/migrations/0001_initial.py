# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=2, choices=[(b'1', b'Publico'), (b'2', b'Privado'), (b'3', b'Social')])),
                ('giro_actividad', models.CharField(max_length=50, blank=True)),
                ('razon_social', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50, blank=True)),
                ('cuidad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50, choices=[(b'Aguascalientes', b'Aguascalientes'), (b'Baja California Norte', b'Baja California Norte'), (b'Baja California Sur', b'Baja California Sur'), (b'Campeche', b'Campeche'), (b'Chiapas', b'Chiapas'), (b'Chihuahua', b'Chihuahua'), (b'Coahuila', b'Coahuila'), (b'Colima', b'Colima'), (b'Distrito Federal', b'Distrito Federal'), (b'Durango', b'Durango'), (b'Estado de Mexico', b'Estado de Mexico'), (b'Guanajuato', b'Guanajuato'), (b'Guerrero', b'Guerrero'), (b'Hidalgo', b'Hidalgo'), (b'Jalisco', b'Jalisco'), (b'Michoacan', b'Michoacan'), (b'Morelos', b'Morelos'), (b'Nayarit', b'Nayarit'), (b'Nuevo Leon', b'Nuevo Leon'), (b'Oaxaca', b'Oaxaca'), (b'Puebla', b'Puebla'), (b'Queretaro', b'Queretaro'), (b'Quintana Roo', b'Quintana Roo'), (b'San Luis Potosi', b'San Luis Potosi'), (b'Sinaloa', b'Sinaloa'), (b'Sonora', b'Sonora'), (b'Tabasco', b'Tabasco'), (b'Tamaulipas', b'Tamaulipas'), (b'Tlaxcala', b'Tlaxcala'), (b'Veracruz', b'Veracruz'), (b'Yucatan', b'Yucatan'), (b'Zacatecas', b'Zacatecas')])),
                ('telefono', models.CharField(max_length=15, blank=True)),
                ('fax', models.CharField(max_length=15, blank=True)),
                ('e_mail', models.EmailField(max_length=254, blank=True)),
                ('url', models.URLField(blank=True)),
                ('sector', models.CharField(blank=True, max_length=2, choices=[(b'Sector Primario', ((b'11', b'Agroindustrial'), (b'12', b'Pesquero'), (b'13', b'Minero'), (b'14', b'Otros'))), (b'Sector Secundario', ((b'21', b'Industrial'), (b'22', b'Constructor'), (b'23', b'Petrolero'), (b'24', b'Otros'))), (b'Sector Terciario', ((b'31', b'Educativo'), (b'32', b'Turismo'), (b'33', b'Comercio'), (b'34', b'Servicios Financieros'), (b'35', b'Otros')))])),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_encargado', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50, blank=True)),
                ('puesto', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='encargado',
            field=models.ForeignKey(to='empresa.Encargado', blank=True),
        ),
    ]
