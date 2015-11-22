# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151108_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.ImageField(upload_to='candidate_pics', blank=True, null=True),
        ),
    ]
