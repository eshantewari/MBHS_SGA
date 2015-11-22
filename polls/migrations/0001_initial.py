# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('candidate_name', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('category_text', models.CharField(max_length=200)),
                ('category_num', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('grade_level', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.IntegerField(serialize=False, primary_key=True)),
                ('grade', models.IntegerField()),
                ('password', models.CharField(null=True, blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='category',
            field=models.ForeignKey(to='polls.Category'),
        ),
    ]
