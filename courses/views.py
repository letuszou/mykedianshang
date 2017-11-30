# coding: utf-8


import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q

from courses.models import Course, CourseResource
from operation.models import CourseComments
from utils.mixin_utils import LoginRequireMixin


class CoursesListView(View):
    """
    课程列表
    """

    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")
        current_page = "course_list"
        current_nav = "course_list"
        hot_courses = Course.objects.all().order_by("-click_num")[:3]
        sort = request.GET.get('sort', "")

        # 课程搜索
        search_keywords = request.GET.get("keywords","")
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))

        if sort:
            if sort == "hot":
                all_courses == all_courses.order_by("click_num")
            elif sort == "students":
                all_courses == all_courses.order_by("students")

        return render(request, 'course_list.html', {
            "all_courses": all_courses,
            "current_page": current_page,
            "sort": sort,
            "hot_courses": hot_courses,
            "current_nav":current_nav
        })


class CourseDetailView(View):
    """
    课程详情
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        org = course.course_org
        course.click_num += 1
        course.save()
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        current_nav = "course_list"

        return render(request, 'course-detail.html', {
            "course": course,
            "relate_courses": relate_courses,
            "org": org,
            "current_nav":current_nav
        })


class CoursesVideoView(View):
    # 课程资源
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        courseResource = CourseResource.objects.filter(course=course)
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:3]
        else:
            relate_courses = []
        current_nav = "course_list"
        return render(request, 'course-video.html', {
            "course_id": course_id,
            "course": course,
            "courseResource": courseResource,
            "relate_courses": relate_courses,
            "current_nav":current_nav
        })


class CoursesCommentView(LoginRequireMixin, View):
    # 课程评论
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        logging.error("id=" + str(course_id))
        course_comments = course.coursecomments_set.all()
        relate_courses = CourseResource.objects.filter(course=course)
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        current_nav = "course_list"
        return render(request, 'course-comment.html', {
            "course_id": course_id,
            "course": course,
            "course_comments": course_comments,
            "relate_courses": relate_courses,
            "current_nav":current_nav

        })


class CoursesAddCommentView(View):
    def post(self, request):
        """
        添加评论
        """
        comment = request.POST.get("comments", "")
        course_id = request.POST.get("course_id", 0)
        if comment:
            createComment = CourseComments()
            createComment.comments = comment
            createComment.course_id = course_id
            createComment.user = request.user
            createComment.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail'}", content_type='application/json')
