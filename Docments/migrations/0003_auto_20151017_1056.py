# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Docments', '0002_auto_20150723_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '档案分类', 'verbose_name_plural': '档案分类'},
        ),
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': '档案', 'ordering': ['full_name'], 'verbose_name_plural': '档案'},
        ),
        migrations.AddField(
            model_name='documents',
            name='photo',
            field=models.ImageField(null=True, verbose_name='档案照片', upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(verbose_name='类别', max_length=70),
        ),
        migrations.AlterField(
            model_name='documents',
            name='category',
            field=models.ForeignKey(to='Docments.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='dead_date',
            field=models.DateTimeField(verbose_name='过期日期'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_no',
            field=models.IntegerField(verbose_name='档案编号'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='full_name',
            field=models.CharField(verbose_name='名称', max_length=100),
        ),
        migrations.AlterField(
            model_name='documents',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布日期'),
        ),
    ]
