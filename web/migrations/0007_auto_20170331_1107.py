# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20170331_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='bktime',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
