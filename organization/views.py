# coding: utf-8


import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from courses.models import Course
from organization.forms import UserAskForm
from organization.models import CourseOrg, CityDict, Teacher

'''机构的列表'''


class OrgListView(View):
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_args = all_orgs.order_by("-click_num")[:3]
        all_citys = CityDict.objects.all()
        city_id = request.GET.get("city", "")
        # 城市机构筛选

        if city_id:
            # django 语言中 model_id 可以去除一个id
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_orgs == all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs == all_orgs.order_by("-course_nums")

        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {
            "all_orgs": all_orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_args": hot_args,
            "sort": sort
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        logging.error("******************************")
        if userask_form.is_valid():
            # commit 设置True会直接和数据库交互
            userask_form.save(commit=True)
            return HttpResponse("{'status':'success}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail,'msg':{0}}".format(userask_form.errors))


class OrgHomeView(View):
    """
    机构首页
    """

    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 外键 反向取数据类名 小写 _set
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page
        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            "teachers": teachers,
            "course_org": course_org,
            "current_page": current_page
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            "course_org": course_org,
            "current_page": current_page
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            "courses": courses,
            "course_org": course_org,
            "current_page": current_page
        })
