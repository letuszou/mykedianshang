# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u540d\u79f0'),
        ),
    ]
