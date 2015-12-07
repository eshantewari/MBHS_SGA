# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151018_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(null=True, upload_to=b'candidate_pics', blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='motto',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='students',
            name='votes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
