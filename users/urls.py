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

from users.views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^loginout/$', LoginOutView.as_view(), name='logout'),
    url(r'^myinfo/$', MyInfoView.as_view(), name='my_info'),
    url(r'^mycourses/$', MyCoursesView.as_view(), name='my_courses'),
    url(r'^mymessage/$', MyMessageView.as_view(), name='my_message'),
    #     用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

]
