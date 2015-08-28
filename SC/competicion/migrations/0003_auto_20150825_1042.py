# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competicion', '0002_piloto_oficial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clasificacion',
            unique_together=set([('gran_premio', 'piloto')]),
        ),
    ]
