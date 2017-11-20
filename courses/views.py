# coding: utf-8


from django.shortcuts import render
from django.views.generic import View

from courses.models import Course


class CoursesListView(View):
    """
    课程列表
    """

    def get(self, request):
        courses = Course.objects.all()
        current_page = "course_list"
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "hot":
                courses == courses.order_by("-click_num")
            elif sort == "join":
                courses == courses.order_by("-students")
        return render(request, 'course_list.html', {
            "courses": courses,
            "current_page": current_page,
            "sort": sort
        })


class CourseDetailView(View):
    """
    课程详情
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        org = course.course_org
        return render(request, 'course-detail.html', {
            "course": course,
            "org": org
        })
