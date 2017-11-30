# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_teacher_age'),
        ('courses', '0006_auto_20171101_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_teacher',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b\u6559\u5e08', blank=True, to='organization.Teacher', null=True),
        ),
    ]
