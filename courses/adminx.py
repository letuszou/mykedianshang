# coding: utf-8

import xadmin

from .models import Course, Lesson, Video,CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'click_num', 'add_time']


class LessonAdmin(object):
    list_display = ['name', 'lesson', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'add_time', 'course']


class CourseResourceAdmin(object):
    list_display = ['name', 'add_time', 'course', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
