# coding: utf-8
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    add_time = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=200, verbose_name=u"描述")

    class Meta:
        db_table = "city_dict"
        verbose_name = "城市"

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    category = models.CharField(default="pxjg", max_length=20, choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")),
                                verbose_name=u"机构类型")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.CharField(max_length=100, verbose_name=u"logo")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "course_org"
        verbose_name = "课程机构"

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_year = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏数")
    age = models.IntegerField(default=0, null=True, verbose_name=u"年龄")
    image = models.CharField(max_length=100, verbose_name=u"教师封面",
                             default="http://bj.bcebos.com/imagelib/150/share_pic/a5dce4cfc0dd4094460859846e9c25fd.jpg")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "teacher"
        verbose_name = "教师"

    def __unicode__(self):
        return self.name
