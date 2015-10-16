# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathbreakers', '0014_auto_20150326_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='unlimited_licenses',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
