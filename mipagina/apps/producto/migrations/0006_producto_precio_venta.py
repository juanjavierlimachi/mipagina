# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20170320_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Precio_venta',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
