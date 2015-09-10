# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engines',
            fields=[
                ('Name', models.CharField(max_length=30)),
                ('Cpus', models.IntegerField()),
                ('Memory', models.IntegerField()),
                ('Addr', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
    ]
