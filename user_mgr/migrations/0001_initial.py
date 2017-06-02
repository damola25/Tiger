# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 10:30
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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_address', models.TextField()),
                ('lga', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Address',
            },
        ),
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friendlist',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'others', b'others')], default='m', max_length=1)),
                ('status', models.CharField(choices=[(b'single', b'single'), (b'married', b'married'), (b'others', b'others')], default='single', max_length=25)),
                ('occupation', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User account',
            },
        ),
        migrations.AddField(
            model_name='friendlist',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_mgr.UserAccount'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_mgr.UserAccount'),
        ),
    ]
