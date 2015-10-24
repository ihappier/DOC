# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('category', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('dead_date', models.DateField()),
                ('doc_no', models.IntegerField()),
                ('category', models.ForeignKey(to='Docments.Category')),
            ],
        ),
    ]
