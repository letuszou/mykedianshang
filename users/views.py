# coding: utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from users.forms import LoginForm
from utils.mixin_utils import LoginRequireMixin
from .models import UserProfile


class LoginUnSafeView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html', {"msg": u"用户名或密码错误"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html', {"msg": u"用户名或密码错误"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class RegisterView(View):
    """
    注册
    """

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user_temp = UserProfile.objects.filter(username=user_name)
        if not user_temp:
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
            return render(request, 'login.html')
        else:
            return render(request, "register.html")


class LoginOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class MyInfoView(View):
    """
    个人中心--我的信息
    """

    def get(self, request):
        return render(request, 'usercenter-info.html')


class MyCoursesView(View):
    """
    我的课程
    """

    def get(self, request):
        return render(request, 'usercenter-mycourse.html')


class MyMessageView(View):
    """
    我的消息
    """

    def get(self, request):
        return render(request, 'usercenter-message.html')


class UploadImageView(LoginRequireMixin, View):
    """
    用户修改头像
    """

    def post(self, request):
        image = request.get("image", "")
        request.user.image = image
        request.user.image.save()
