# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20141207_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='iplist',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=32)),
                ('port', models.CharField(max_length=32)),
                ('ver', models.CharField(max_length=32)),
                ('buffer', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'iplist',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='userinfo',
        ),
    ]
