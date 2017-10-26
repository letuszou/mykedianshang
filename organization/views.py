# coding: utf-8


from django.shortcuts import render,render_to_response
from django.views.generic import View

from organization.models import CourseOrg, CityDict

# Create your views here.

'''机构的列表'''


class OrgView(View):
    def get(self, request):
        # 课程机构
        all_args = CourseOrg.objects.all()
        org_nums = all_args.count()
        all_citys = CityDict.objects.all()
        return render(request, 'org-list.html', {
            "all_args": all_args,
            "all_citys": all_citys,
            "org_nums": org_nums
        })
