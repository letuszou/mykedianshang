# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from blog.models import Article


class BlogIndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'blog_index.html', {
            "articles": articles
        })


class BlogWriteView(View):
    def get(self, request):
        return render(request, 'blog_write.html')

    def post(self, request):
        content = request.POST.get("content", "")
        title = request.POST.get("title", "")
        if content:
            artical = Article()
            artical.content = content
            artical.title = title
            artical.save()
            return HttpResponse('{"status":"0","detail":"success"}')
        else:
            return HttpResponse('{"status":"1","detail":"fail"}')


class BlogEditView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        return render(request, 'blog_edit.html', {
            "article": article
        })

    def post(self, request, article_id):
        content = request.POST.get("content", "")
        title = request.POST.get("title", "")
        if article_id:
            article = Article.objects.get(id=int(article_id))
            article.content = content
            article.title = title
            article.save()
            return HttpResponse('{"status":"0","detail":"success"}')
        else:
            return HttpResponse('{"status":"1","detail":"fail"}')
