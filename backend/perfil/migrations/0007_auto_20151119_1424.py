# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_auto_20151118_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoslaborales',
            name='anio_ingr_laboral',
            field=models.DateField(null=True, blank=True),
        ),
    ]
