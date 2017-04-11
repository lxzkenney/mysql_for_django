#!/usr/bin/env python
#coding:utf-8

from django.db import models

class UserInfo(models.Model):
    Nid = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=256)
    RealName =  models.CharField(max_length=256)
    Email = models.EmailField(max_length=256)
    