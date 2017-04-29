# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='Coutas',
            new_name='Total',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='fecha_de_pago',
        ),
        migrations.AddField(
            model_name='reserva',
            name='adelanto',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
