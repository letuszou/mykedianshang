# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20171013_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '\u8bfe\u7a0b'},
        ),
        migrations.AlterModelOptions(
            name='courseresource',
            options={'verbose_name': '\u89c6\u9891\u8d44\u6e90'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '\u7ae0\u8282'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '\u89c6\u9891'},
        ),
        migrations.AlterModelTable(
            name='course',
            table='courses',
        ),
        migrations.AlterModelTable(
            name='courseresource',
            table='course_resource',
        ),
        migrations.AlterModelTable(
            name='lesson',
            table='lesson',
        ),
        migrations.AlterModelTable(
            name='video',
            table='video',
        ),
    ]
