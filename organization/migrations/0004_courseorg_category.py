# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20171026_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(default=b'pxjg', max_length=20, verbose_name='\u673a\u6784\u7c7b\u578b', choices=[(b'pxjg', b'\xe5\x9f\xb9\xe8\xae\xad\xe6\x9c\xba\xe6\x9e\x84'), (b'gr', b'\xe4\xb8\xaa\xe4\xba\xba'), (b'gx', b'\xe9\xab\x98\xe6\xa0\xa1')]),
        ),
    ]
