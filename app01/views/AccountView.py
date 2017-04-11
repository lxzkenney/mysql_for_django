#!/usr/bin/env python
#coding:utf-8
'''
Created on 2014年11月25日

@author: Administrator
@brief : 登录、注册、注销
'''
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from django.template.context import RequestContext 
from app01.models import *
from app01.forms.AccountForm import LoginForm


def Login(request):
    data = {'LoginStatus':''}
    if request.method == 'POST':
        postData = request.POST
        username = postData.get('username')
        password = postData.get('password')
        if username and password:
            result = UserInfo.objects.filter(UserName=username,Password=password)
            if result == 1:
                request.session["LoginModel"] = UserInfo.objects.get(UserName=username,Password=password)
                return redirect('/admin/index')
    data['LoginStatus'] = '用户名或密码错误.'
    return render_to_response('Account/Login.html',data,context_instance=RequestContext(request))

def LoginByForm(request):
    data = request.POST
    loginForm = LoginForm(data)
    
    if loginForm.is_valid():
        return HttpResponse('OK')
    else:
        return render_to_response('Account/LoginForm.html',context_instance=RequestContext(request))
        
def Logout(request):
    pass

def Register(request):
    pass

    
    
    
    
    