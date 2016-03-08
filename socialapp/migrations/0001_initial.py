# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 20:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog', models.TextField()),
                ('activity', models.CharField(choices=[('h', 'Hiking'), ('r', 'Running'), ('b', 'Mountain Biking'), ('c', 'Climbing'), ('s', 'Skiing')], max_length=30)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-post_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=50)),
                ('friends', models.ManyToManyField(related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(to='socialapp.Post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(to='socialapp.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
