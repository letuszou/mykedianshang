# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20171013_1919'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=200, verbose_name='\u8bc4\u8bba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_comments',
                'verbose_name': '\u8bfe\u7a0b\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a')),
                ('course_name', models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'user_ask',
                'verbose_name': '\u7528\u6237\u54a8\u8be2',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5b66\u4e60\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_course',
                'verbose_name': '\u7528\u6237\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eid')),
                ('fav_type', models.IntegerField(default=1, verbose_name='\u6536\u85cf\u7c7b\u578b', choices=[(1, b'\xe8\xaf\xbe\xe7\xa8\x8b'), (2, b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x9c\xba\xe6\x9e\x84'), (3, b'\xe8\xae\xb2\xe5\xb8\x88')])),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_favorite',
                'verbose_name': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.IntegerField(default=0, verbose_name='\u63a5\u6536\u7528\u6237')),
                ('message', models.CharField(max_length=500, verbose_name='\u8be6\u7ec6\u5185\u5bb9')),
                ('has_read', models.BooleanField(default=False, max_length=2, verbose_name='\u662f\u5426\u5df2\u8bfb\u8fc7')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'use_message',
                'verbose_name': '\u7528\u6237\u6d88\u606f',
            },
        ),
    ]
