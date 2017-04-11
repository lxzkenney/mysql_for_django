#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render, render_to_response
from django.shortcuts import render
from django.http import HttpResponse
import json
import MySQLdb
import sys
import paramiko

def Index(request):
    return HttpResponse('<h1>Web.Index</h1>')




