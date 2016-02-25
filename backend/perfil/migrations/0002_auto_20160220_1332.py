# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilegresado',
            name='domicilio',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='perfilegresado',
            name='otros_idms',
            field=models.CharField(max_length=50),
        ),
    ]
