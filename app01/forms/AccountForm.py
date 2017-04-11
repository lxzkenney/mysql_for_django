#!/usr/bin/env python
#coding:utf-8
'''
Created on 2014年12月5日

@author: Administrator
'''

from django import forms
#from django import forms.ModelForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    