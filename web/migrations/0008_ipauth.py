# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170331_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ipauth',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('port', models.CharField(max_length=12)),
                ('extra', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ipauth',
            },
            bases=(models.Model,),
        ),
    ]
