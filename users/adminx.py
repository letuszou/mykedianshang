# coding: utf-8

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


# 设置xadmin主题
class BaseSetting(object):
    enable_themes = True
    use_booswatch = True


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "官网"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']


class BannerAdmin(object):
    list_display = ['title', 'index', 'add_time', 'url', 'image']
    search_fields = ['title']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
