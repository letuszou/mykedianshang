# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '\u7ae0\u8282', 'verbose_name_plural': '\u7ae0\u8282'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '\u89c6\u9891', 'verbose_name_plural': '\u89c6\u9891'},
        ),
    ]
