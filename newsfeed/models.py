# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    password = models.CharField(max_length=32)

class MyUser(models.Model):
    user_name = models.OneToOneField(User)
    email = models.EmailField(default='email', max_length=255, unique=True, blank=False)

    def __unicode__(self):
        return u'{}'.format(self.email)
