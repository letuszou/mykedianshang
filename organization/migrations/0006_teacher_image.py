# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20171027_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.CharField(default=b'http://bj.bcebos.com/imagelib/150/share_pic/a5dce4cfc0dd4094460859846e9c25fd.jpg', max_length=100, verbose_name='\u6559\u5e08\u5c01\u9762'),
        ),
    ]
