# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_video_learn_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.CharField(max_length=100, verbose_name='\u8d44\u6e90\u6587\u4ef6'),
        ),
    ]
