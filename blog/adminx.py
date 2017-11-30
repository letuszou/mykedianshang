# coding: utf-8

import xadmin

from .models import Tag, Article


class TagAdmin(object):
    list_display = ['name']


class ArticleAdmin(object):
    list_display = ['title', 'desc', 'content', 'click_count', 'add_time']


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)
