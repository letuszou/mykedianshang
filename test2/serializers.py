# coding: utf-8
from rest_framework import serializers

from courses.models import Course


class TestSerializer(serializers.ModelSerializer):
    real_sub_price = serializers.CharField(max_length=1024, source='get_sub_price', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'detail',
        ]
        read_only_fields = ('id')
