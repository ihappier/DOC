# coding utf-8
from django.db import models
from django.utils import timezone
import datetime


# STATUS_CHOICES = (
#     ('d', 'Draft'),
#     ('p', 'Published'),
#     ('w', 'Withdrawn'),
# )
# Create your models here.


class Category(models.Model):
    category = models.CharField('类别', max_length=70)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = '档案分类'
        verbose_name_plural = '档案分类'


# 建立档案类，包含所属分类，名称，发布日期，过期日期，档案编号，照片


class Documents(models.Model):
    category = models.ForeignKey(Category, verbose_name='类别')
    full_name = models.CharField('名称', max_length=100)
    pub_date = models.DateTimeField('发布日期')
    dead_date = models.DateTimeField('过期日期')
    doc_no = models.IntegerField('档案编号')
    photo = models.ImageField('档案照片', null=True)
    # status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def was_over_date(self):
        return self.dead_date >= timezone.now() + datetime.timedelta(days=3)

    # was_over_date.admin_order_field = pub_date
    was_over_date.boolean = True
    was_over_date.short_description = '过期'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = '档案'
        verbose_name_plural = '档案'
        ordering = ['full_name']