# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20151118_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilegresado',
            name='mes_anio_egreso',
            field=models.DateField(),
        ),
    ]
