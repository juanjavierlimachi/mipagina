# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20170311_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(default='2015-05-05'),
            preserve_default=False,
        ),
    ]
