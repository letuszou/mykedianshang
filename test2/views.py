# coding: utf-8

from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from courses.models import Course
from organization.models import CourseOrg


def home(request):
    orgs = CourseOrg.objects.all()[:12]
    middle_class = ["module1_3", "module1_4", "module1_5", "module1_6", "module1_7", "module1_8"]
    courses = Course.objects.all()[:6]
    hot_courses = Course.objects.all().order_by("-students")[:5]
    click_courses = Course.objects.all().order_by("-click_num")[:3]
    current_nav = "index"

    return render(request, 'index.html', {
        "orgs": orgs,
        "middle_class": middle_class,
        "courses": courses,
        "current_nav": current_nav,
        "hot_courses": hot_courses,
        "click_courses": click_courses
    })


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'category', 'learn_time', 'add_time')


class ListTestApiView(ListAPIView):
    """
    第一个get请求的接口，希望一切都好(注释)\n
    ListTestApiView 显示了前三个单词
    """
    serializer_class = ListSerializer

    def get_queryset(self):
        return Course.objects.all()

    def post(self):
        pass


def permission_denied(request):
    # 全局403处理函数
    response = render_to_response('403.html', {})
    response.status_code = 403
    return response


def page_not_found(request):
    # 全局404处理函数
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
