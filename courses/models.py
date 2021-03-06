# coding: utf-8

from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    course_teacher = models.ForeignKey(Teacher, verbose_name=u"课程教师", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=3, choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")))
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.CharField(max_length=100, verbose_name=u"课程图片")
    click_num = models.IntegerField(default=0, verbose_name=u"课程点击量")
    category = models.CharField(max_length=20, default="后端开发", verbose_name=u"课程类型")
    tag = models.CharField(max_length=20, default="", verbose_name=u"课程标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        db_table = 'courses'
        verbose_name = "课程"

    # 获取课程章节数
    def get_zj_nums(self):
        return self.lesson_set.all().count()

    # 获取学习人数
    def get_learn_num(self):
        return self.usercourse_set.all()[:5]

    # 获取课程的章节
    def get_course_lesson(self):
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")

    def get_lesson_video(self):
        return self.video_set.all()

    class Meta:
        db_table = 'lesson'
        verbose_name = "章节"

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, verbose_name=u"访问地址", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")

    class Meta:
        db_table = 'video'
        verbose_name = "视频"

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    download = models.CharField(max_length=100, verbose_name=u"资源文件")

    class Meta:
        db_table = 'course_resource'
        verbose_name = "视频资源"

    def __unicode__(self):
        return self.name
