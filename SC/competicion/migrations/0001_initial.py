# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField()),
                ('pos_latitud', models.FloatField()),
                ('pos_longitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posicion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Escuderia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField()),
                ('fecha_fundacion', models.DateField()),
                ('empleados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GranPremio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('circuito', models.ForeignKey(to='competicion.Circuito')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField()),
                ('apellidos', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_victorias', models.IntegerField()),
                ('numero_podios', models.IntegerField()),
                ('escuderia', models.ForeignKey(to='competicion.Escuderia')),
                ('persona', models.ForeignKey(to='competicion.Persona')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together=set([('nombre', 'apellidos', 'fecha_nacimiento')]),
        ),
        migrations.AddField(
            model_name='escuderia',
            name='duenio',
            field=models.ForeignKey(to='competicion.Persona'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='gran_premio',
            field=models.ForeignKey(to='competicion.GranPremio'),
        ),
        migrations.AddField(
            model_name='clasificacion',
            name='piloto',
            field=models.ForeignKey(to='competicion.Piloto'),
        ),
        migrations.AlterUniqueTogether(
            name='circuito',
            unique_together=set([('nombre', 'pos_latitud', 'pos_longitud', 'longitud')]),
        ),
        migrations.AlterUniqueTogether(
            name='piloto',
            unique_together=set([('persona', 'escuderia', 'numero_victorias', 'numero_podios')]),
        ),
        migrations.AlterUniqueTogether(
            name='granpremio',
            unique_together=set([('circuito', 'fecha')]),
        ),
        migrations.AlterUniqueTogether(
            name='escuderia',
            unique_together=set([('nombre', 'fecha_fundacion', 'empleados', 'duenio')]),
        ),
        migrations.AlterUniqueTogether(
            name='clasificacion',
            unique_together=set([('gran_premio', 'piloto', 'posicion')]),
        ),
    ]
