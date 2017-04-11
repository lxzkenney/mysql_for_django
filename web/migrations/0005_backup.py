# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170328_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='backup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=32)),
                ('bktime', models.DateTimeField()),
                ('bkname', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'backup',
            },
            bases=(models.Model,),
        ),
    ]
