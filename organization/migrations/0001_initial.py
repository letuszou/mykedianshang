# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u57ce\u5e02')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=200, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'db_table': 'city_dict',
                'verbose_name': '\u57ce\u5e02',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u673a\u6784\u540d\u79f0')),
                ('desc', models.TextField(verbose_name='\u673a\u6784\u63cf\u8ff0')),
                ('click_num', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('fav_num', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('image', models.ImageField(upload_to=b'org/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('address', models.CharField(max_length=150, verbose_name='\u673a\u6784\u5730\u5740')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(verbose_name='\u6240\u5728\u57ce\u5e02', to='organization.CityDict')),
            ],
            options={
                'db_table': 'course_org',
                'verbose_name': '\u8bfe\u7a0b\u673a\u6784',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u6559\u5e08\u540d\u79f0')),
                ('work_year', models.IntegerField(default=0, verbose_name='\u5de5\u4f5c\u5e74\u9650')),
                ('work_company', models.CharField(max_length=50, verbose_name='\u5c31\u804c\u516c\u53f8')),
                ('work_position', models.CharField(max_length=50, verbose_name='\u516c\u53f8\u804c\u4f4d')),
                ('points', models.CharField(max_length=50, verbose_name='\u6559\u5b66\u7279\u70b9')),
                ('fav_num', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', to='organization.CourseOrg')),
            ],
            options={
                'db_table': 'teacher',
                'verbose_name': '\u6559\u5e08',
            },
        ),
    ]
