# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_reserva_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='archivo',
            field=models.FileField(null=True, upload_to=b'productos', blank=True),
        ),
    ]
