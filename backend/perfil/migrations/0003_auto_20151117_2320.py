# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20151117_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilegresado',
            name='f_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='perfilegresado',
            name='mes_anio_egreso',
            field=models.DateField(blank=True),
        ),
    ]
