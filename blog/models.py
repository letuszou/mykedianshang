# coding: utf-8

from datetime import datetime

from django.db import models


# 文章模型
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"标签名称")

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"文章标题")
    desc = models.CharField(max_length=50, verbose_name=u"文章描述")
    content = models.TextField(verbose_name=u"文章内容")
    click_count = models.IntegerField(default=0, verbose_name=u"点击次数")
    tag = models.ManyToManyField(Tag, verbose_name=u"标签")
    add_time = models.DateTimeField(default=datetime.now)
    image = models.CharField(max_length=100, verbose_name=u"文章封面",
                             default="http://bj.bcebos.com/imagelib/150/share_pic/a5dce4cfc0dd4094460859846e9c25fd.jpg")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
