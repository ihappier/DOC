# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Docments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='dead_date',
            field=models.DateTimeField(verbose_name='date_overtime'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]
