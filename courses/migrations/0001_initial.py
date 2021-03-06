# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('desc', models.CharField(max_length=300, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('detail', models.TextField(verbose_name='\u8bfe\u7a0b\u8be6\u60c5')),
                ('degree', models.CharField(max_length=3, choices=[(b'cj', b'\xe5\x88\x9d\xe7\xba\xa7'), (b'zj', b'\xe4\xb8\xad\xe7\xba\xa7'), (b'gj', b'\xe9\xab\x98\xe7\xba\xa7')])),
                ('learn_time', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f\u6570)')),
                ('students', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('image', models.ImageField(upload_to=b'courses/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('click_num', models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u70b9\u51fb\u91cf')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'courses',
                'verbose_name': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('download', models.FileField(upload_to=b'course/resource/%Y/%m', verbose_name='\u8d44\u6e90\u6587\u4ef6')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
            ],
            options={
                'db_table': 'course_resource',
                'verbose_name': '\u89c6\u9891\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u7ae0\u8282\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
            ],
            options={
                'db_table': 'lesson',
                'verbose_name': '\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('lesson', models.ForeignKey(verbose_name='\u7ae0\u8282', to='courses.Lesson')),
            ],
            options={
                'db_table': 'video',
                'verbose_name': '\u89c6\u9891',
            },
        ),
    ]
