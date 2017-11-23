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
import xadmin
from django.conf.urls import include

import views
from test2.views import *
from users.urls import url

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^$', views.home),
    url(r'^account/', include('users.urls')),
    url(r'^org/', include('organization.urls', namespace='org')),
    url(r'^course/', include('courses.urls', namespace='course')),
    url(r'^test/list/', ListTestApiView.as_view(),name='list_list'),
]
