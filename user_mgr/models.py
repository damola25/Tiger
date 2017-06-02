# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from model_field_choices import USER_STATUS, GENDER
# Create your models here.

class FriendList(models.Model):
    owner           =       models.OneToOneField('UserAccount')
    friends         =       models.ForeignKey(User)

    class Meta:
        verbose_name = "Friendlist"

class Address(models.Model):
    user                     =       models.ForeignKey('UserAccount')
    house_address            =       models.TextField()
    lga                      =       models.CharField(max_length = 150)
    state                    =       models.CharField(max_length = 150)
    country                  =       models.CharField(max_length = 150)

    class Meta:
        verbose_name = "Address"

    def __unicode__(self):
        return '%s' %(self.house_address)


class UserAccount(models.Model):
    user            =       models.OneToOneField(User)
    phone_number    =       models.IntegerField(default = 0)
    gender          =       models.CharField(max_length = 1, choices = GENDER, default='m')
    status          =       models.CharField(max_length = 25, choices = USER_STATUS, default = 'single')
    occupation      =       models.CharField(max_length = 150, null=True, blank=True)

    class Meta:
        verbose_name = "User account"

    def __str__(self):
        return self.user.username
