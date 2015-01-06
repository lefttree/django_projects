# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tagging.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Maximum 250 characters.', max_length=250)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique.', unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique.', unique_for_date=b'pub_date')),
                ('enable_comments', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Live'), (2, b'Draft'), (3, b'Hidden')])),
                ('tags', tagging.fields.TagField(max_length=255, blank=True)),
                ('excerpt_html', models.TextField(editable=False, blank=True)),
                ('body_html', models.TextField(editable=False, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='bruno.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
