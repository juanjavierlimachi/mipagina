# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '__first__'),
        ('cliente', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_categoria', models.CharField(unique=True, max_length=50)),
                ('Material', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompraProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Precio_unidad', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.FloatField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_producto', models.CharField(unique=True, max_length=150)),
                ('Marca', models.CharField(max_length=50)),
                ('Precio_producto', models.FloatField()),
                ('Stock', models.IntegerField(default=0)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('archivo', models.FileField(upload_to=b'productos')),
                ('Categoria', models.ForeignKey(to='producto.Categoria')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SalidasPro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Precio_unidad', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.FloatField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=0)),
                ('producto', models.ForeignKey(to='producto.Producto')),
                ('trabajador', models.ForeignKey(to='cliente.Trabajador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='compraproducto',
            name='producto',
            field=models.ForeignKey(to='producto.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compraproducto',
            name='proveedor',
            field=models.ForeignKey(to='proveedor.Proveedor'),
            preserve_default=True,
        ),
    ]
