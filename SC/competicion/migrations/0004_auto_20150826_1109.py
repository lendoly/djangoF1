# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competicion', '0003_auto_20150825_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clasificacion',
            options={'verbose_name': 'Clasificacion', 'verbose_name_plural': 'Clasificaciones'},
        ),
        migrations.AlterModelOptions(
            name='granpremio',
            options={'verbose_name': 'Gran Premio', 'verbose_name_plural': 'Grandes Premios'},
        ),
        migrations.AlterModelOptions(
            name='piloto',
            options={'verbose_name': 'Piloto', 'verbose_name_plural': 'Pilotos'},
        ),
        migrations.AddField(
            model_name='circuito',
            name='imagen',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
