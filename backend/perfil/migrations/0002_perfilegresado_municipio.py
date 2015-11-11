# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilegresado',
            name='municipio',
            field=models.CharField(default='TEHUACAN', max_length=50),
            preserve_default=False,
        ),
    ]
