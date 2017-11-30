# coding: utf-8

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from courses.models import Course
from operation.models import UserFavorite
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
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords))
        org_nums = all_orgs.count()
        current_page = "org_list"
        current_nav = "org_list"
        return render(request, 'org-list.html', {
            "all_orgs": all_orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_args": hot_args,
            "sort": sort,
            "current_page": current_page,
            "current_nav": current_nav
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
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
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
            else:
                has_fav = False
        else:
            return render(request, 'login.html')

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        current_nav = "org_list"
        return render(request, 'org-detail-homepage.html', {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
            "current_nav": current_nav

        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = "teacher"
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav = True
            else:
                has_fav = False
        else:
            return render(request, 'login.html')
        course_org = CourseOrg.objects.get(id=int(org_id))
        teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            "teachers": teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = "desc"
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav = True
            else:
                has_fav = False
        else:
            return render(request, 'login.html')
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        courses = course_org.course_set.all()
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav = True
            else:
                has_fav = False
        else:
            return render(request, 'login.html')
        return render(request, 'org-detail-course.html', {
            "courses": courses,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class AddUserFavView(View):
    """
    用户收藏以及用户取消收藏
    """

    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        if not request.user.is_authenticated:
            return HttpResponse("{'status':'fail,'msg':'用户未登录'}")
        exist_records = UserFavorite.objects.filter(user_id=request.user.id, fav_id=int(fav_id), fav_type=int(fav_type))
        # 如果记录已经存在，则表示用户取消收藏
        if exist_records:
            exist_records.delete()
            return HttpResponse("{'status':'success,'msg':'取消收藏'}", content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse("{'status':'success,'msg':'收藏成功'}", content_type='application/json')
            else:
                return HttpResponse("{'status':'fail','msg':'收藏出错'}", content_type='application/json')


class TeachersView(View):
    def get(self, request):
        current_page = "org_teachers"
        # 课程搜索
        search_keywords = request.GET.get("keywords", "")
        teachers = Teacher.objects.all()
        if search_keywords:
            teachers = teachers.filter(Q(name__icontains=search_keywords))
        hot_teachers = Teacher.objects.all()[:3]
        count = teachers.count()
        current_nav = "org_teachers"

        return render(request, 'teachers-list.html', {
            "current_page": current_page,
            "teachers": teachers,
            "count": count,
            "hot_teachers": hot_teachers,
            "current_nav": current_nav
        })


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        current_page = "teacher_detail"
        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher_courses = Course.objects.filter(course_teacher=teacher)[:3]
        org_teachers = Teacher.objects.filter(org=teacher.org)[:3]
        current_nav = "org_teachers"

        return render(request, 'teacher-detail.html', {
            "current_page": current_page,
            "teacher": teacher,
            "teacher_courses": teacher_courses,
            "org_teachers": org_teachers,
            "current_nav": current_nav
        })
