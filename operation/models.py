# coding: utf-8
from datetime import datetime

from django.db import models

from courses.models import Course
from users.models import UserProfile


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        db_table = "user_ask"
        verbose_name = "用户咨询"

    def __unicode__(self):
        return self.name


class CourseComments(models.Model):
    """课程评论"""
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        db_table = "course_comments"
        verbose_name = "课程评论"

    def __unicode__(self):
        return self.user.username


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(default=1, choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        db_table = "user_favorite"
        verbose_name = "用户收藏"

    def __unicode__(self):
        return self.user


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"详细内容")
    has_read = models.BooleanField(max_length=2, default=False, verbose_name=u"是否已读过")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        db_table = "use_message"
        verbose_name = "用户消息"

    def __unicode__(self):
        return self.user


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"学习时间")

    class Meta:
        db_table = "user_course"
        verbose_name = "用户课程"

    def __unicode__(self):
        return self.user
