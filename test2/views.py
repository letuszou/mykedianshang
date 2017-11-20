# coding: utf-8

from django.shortcuts import render

from courses.models import Course
from organization.models import CourseOrg


def home(request):
    orgs = CourseOrg.objects.all()[:12]
    middle_class = ["module1_3", "module1_4", "module1_5", "module1_6", "module1_7", "module1_8"]
    courses = Course.objects.all()[:6]
    current_page = "index"

    return render(request, 'index.html', {
        "orgs": orgs,
        "middle_class": middle_class,
        "courses": courses,
        "current_page":current_page
    })
