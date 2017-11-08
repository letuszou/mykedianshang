# coding: utf-8
from django.forms import ModelForm

from operation.models import UserAsk


class UserAskForm(ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
