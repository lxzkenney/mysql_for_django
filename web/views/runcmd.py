from django.shortcuts import render, render_to_response
from django.http  import HttpResponse
import json
import MySQLdb
import sys,datetime,time
import paramiko
from web import models
from web.models import ipauth





def sshlogin(hostname,username,password,port,cmd):
    ssh=paramiko.SSHClient() 
    ssh.load_system_host_keys() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(hostname=hostname,username=username,password=password,port=int(port)) 
    stdin1,stdout1,stderr1=ssh.exec_command(cmd,timeout=10)
    info=stdout1.read()
    print stdout1.read()
    return info
    ssh.close()
    
    
def cmdindex(request):
    result='kenney is here'
    ipauth=models.ipauth.objects.all()
    return render_to_response('checkcmd/result.html',{'names':ipauth})


def cmdresult(request):    
    postData = request.POST
    lip = postData.get('select1')
    lcmd = postData.get('cmdinput')
    t=ipauth.objects.get(ip=lip)
    hostname=t.ip
    username=t.username
    password=t.password
    port=t.port
    cmd=lcmd
    ip_list=[]
    info=[]
    
    ssh=paramiko.SSHClient() 
    ssh.load_system_host_keys() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(hostname=hostname,username=username,password=password,port=int(port)) 
    stdin1,stdout1,stderr1=ssh.exec_command(cmd,timeout=10)
    info=stdout1.read().replace('\n','\n\t')
    ssh.close()
    
    tt=models.ipauth.objects.all()
    return render_to_response('checkcmd/result.html',{'key1':info,'names':tt})

    
def checkcmd(request):
    postData = request.POST
    ip = postData.get('ip')
    version = postData.get('version')    
    port = postData.get('port')   
    buff = postData.get('buffer')
    
    lip= postData.get('lip')
    lusername= postData.get('lusername')
    lpassword= postData.get('lpassword')
    lport= postData.get('lport')

    cmd="sh /opt/software/mysql_install.sh -v%s -p%s -s%s" %(version,port,buff)
    sshlogin(lip,lusername,lpassword,lport,cmd)


