# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0002_tweet_usuario_twitter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario_Twitter',
        ),
        migrations.AddField(
            model_name='usuariotwitter',
            name='biografia',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuariotwitter',
            name='nombre',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
