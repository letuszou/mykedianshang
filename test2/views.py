# coding: utf-8

from django.shortcuts import render

from organization.models import CourseOrg


def home(request):
    orgs = CourseOrg.objects.all()[:12]

    return render(request, 'index.html', {
        "orgs": orgs
    })
