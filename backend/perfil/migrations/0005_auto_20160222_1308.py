# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20160220_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoslaborales',
            name='asoc_egresados',
            field=models.CharField(blank=True, max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')]),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='comentarios',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='cual_tp',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='cuales_op',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='cuales_os',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='cuales_tc',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='egresado',
            field=models.ForeignKey(blank=True, to='perfil.PerfilEgresado', null=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='num_control',
            field=models.CharField(max_length=9, blank=True),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='tomar_curso',
            field=models.CharField(default=b'1', max_length=2, blank=True, choices=[(b'1', b'Si'), (b'2', b'No')]),
        ),
        migrations.AlterField(
            model_name='datoslaborales',
            name='tomar_posgrado',
            field=models.CharField(blank=True, max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')]),
        ),
        migrations.AlterField(
            model_name='perfilegresado',
            name='titulado',
            field=models.CharField(default=b'1', max_length=2, null=True, blank=True, choices=[(b'1', b'Si'), (b'0', b'No')]),
        ),
    ]
