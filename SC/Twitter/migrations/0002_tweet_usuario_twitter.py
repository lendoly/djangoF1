# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_tweet', models.BigIntegerField(unique=True)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('usuario', models.ForeignKey(to='Twitter.UsuarioTwitter')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Twitter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField()),
                ('screen_name', models.TextField()),
                ('biografia', models.TextField()),
                ('id_twitter', models.BigIntegerField(unique=True)),
            ],
        ),
    ]
