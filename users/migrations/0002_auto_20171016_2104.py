# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '\u90ae\u7bb1\u9a8c\u8bc1\u7801', 'verbose_name_plural': '\u90ae\u7bb1\u9a8c\u8bc1\u7801'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'male', max_length=6, choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterModelTable(
            name='emailverifyrecord',
            table=None,
        ),
    ]
