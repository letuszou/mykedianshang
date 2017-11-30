# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default=b'\xe5\x90\x8e\xe7\xab\xaf\xe5\xbc\x80\xe5\x8f\x91', max_length=20, verbose_name='\u8bfe\u7a0b\u7c7b\u578b'),
        ),
    ]
