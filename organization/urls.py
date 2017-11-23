# coding: utf-8
"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from organization.views import OrgListView, AddUserAskView, OrgHomeView, OrgTeacherView, OrgDescView, OrgCourseView, \
    AddUserFavView, TeachersView, TeacherDetailView
# from organization.views import *
# begin to serializer
# restframework

# 1. import modules
from django.conf.urls import url, include
from .models import *
from rest_framework import routers, serializers, viewsets

# 2. choose what you want
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseOrg
        fields = ('name',)

# 3. choose how many data you want
class UserViewSet(viewsets.ModelViewSet):
    queryset = CourseOrg.objects.all()
    serializer_class = UserSerializer

# 4. register in app
router = routers.DefaultRouter()

# 5. choose a name, just like urlpatterns
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    # 机构收藏
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^add_fav/$', AddUserFavView.as_view(), name='add_fav'),
    url(r'^teachers/$', TeachersView.as_view(), name='org_teachers'),
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),

]
