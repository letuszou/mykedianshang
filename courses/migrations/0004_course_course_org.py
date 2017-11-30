# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20171027_1956'),
        ('courses', '0003_auto_20171013_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b\u673a\u6784', blank=True, to='organization.CourseOrg', null=True),
        ),
    ]
