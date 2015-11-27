# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_auto_20151118_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoslaborales',
            name='anio_ingr_laboral',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='perfilegresado',
            name='mes_anio_egreso',
            field=models.DateField(blank=True),
        ),
    ]
