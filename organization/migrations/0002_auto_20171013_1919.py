# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citydict',
            options={'verbose_name': '\u57ce\u5e02'},
        ),
        migrations.AlterModelOptions(
            name='courseorg',
            options={'verbose_name': '\u8bfe\u7a0b\u673a\u6784'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '\u6559\u5e08'},
        ),
        migrations.AlterModelTable(
            name='citydict',
            table='city_dict',
        ),
        migrations.AlterModelTable(
            name='courseorg',
            table='course_org',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
    ]
