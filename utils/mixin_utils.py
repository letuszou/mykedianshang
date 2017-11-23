# coding: utf-8


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 继承这个类，当没有登录的时候定向到login_url
class LoginRequireMixin(object):
    @method_decorator(login_required(login_url="/account/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequireMixin, self).dispatch(self, request, *args, **kwargs)
