# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '__first__'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Coutas', models.PositiveIntegerField()),
                ('fecha_de_pago', models.DateField()),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_trabajador', models.ForeignKey(to='cliente.Trabajador')),
                ('producto', models.ForeignKey(to='producto.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
