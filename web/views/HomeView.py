#!/usr/bin/env python
#coding:utf-8
'''
Created on 2014年12月1日

@author: Administrator
'''
from django.shortcuts import render_to_response, redirect
from web.models import UserInfo
from django.http.response import HttpResponse
from django.template.context import RequestContext
from web.Extensions.HtmlHelper import Pager

def Index(request):
    return render_to_response('Home/Index.html')

def UserList(request):
    result = UserInfo.objects.all()
    page = Pager("http://127.0.0.1:8000/admin/userlist/", 2, 90, 180, 20)
    return render_to_response('Home/UserList.html',{'model':result,'page':page},context_instance=RequestContext(request))

def UserDetail(request,id):
    result = UserInfo.objects.get(Nid=int(id))
    return render_to_response('Home/UserDetail.html',{'key1':result})

def AddUser(request):
    postData = request.POST
    #nid = postData.get('nid')
    username = postData.get('username')
    name = postData.get('name')
    gender = postData.get('gender')
    gender2 = postData.get('gender2')
    password = postData.get('password')
    email = postData.get('email')
    if username and name and password and email:
            userInfo = UserInfo(UserName = username,Password=password,RealName = name,Email = email)
            userInfo.save()
        #if int(nid) == 0: 
        #    userInfo = UserInfo(UserName = username,Password=password,RealName = name,Email = email,Gender = gender)
        #    userInfo.save()
        #else:
        #    UserInfo.objects.filter(Nid = nid).update(UserName = username,Password=password,RealName = name,Email = email,Gender = gender)
    return redirect('/admin/userlist')


def DelUser(request):
    postData = request.POST
    nid =  postData.get('delnid')
    nid = int(nid)
    UserInfo.objects.filter(Nid=nid).delete()
    return redirect('/admin/userlist')