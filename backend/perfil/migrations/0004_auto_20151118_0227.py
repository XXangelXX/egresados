# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_auto_20151117_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoslaborales',
            name='anio_ingr_laboral',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='perfilegresado',
            name='f_nacimiento',
            field=models.DateField(blank=True),
        ),
    ]
