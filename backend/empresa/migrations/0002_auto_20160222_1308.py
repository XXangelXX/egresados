# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='datoslaborales',
            field=models.ForeignKey(blank=True, to='perfil.DatosLaborales', null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='num_control',
            field=models.CharField(max_length=9, blank=True),
        ),
        migrations.AlterField(
            model_name='encargado',
            name='empresa',
            field=models.ForeignKey(blank=True, to='empresa.Empresa', null=True),
        ),
        migrations.AlterField(
            model_name='encargado',
            name='num_control',
            field=models.CharField(max_length=9, blank=True),
        ),
    ]
