# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20151108_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='motto',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
