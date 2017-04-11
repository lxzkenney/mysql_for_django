from django.shortcuts import render, render_to_response
from django.http  import HttpResponse
import json
import MySQLdb
import sys,datetime,time
import paramiko
from web import models
from web.models import ipauth


def manage(request):
    return render_to_response('Home/manage.html')

def sshlogin(hostname,username,password,port,cmd):
    ssh=paramiko.SSHClient() 
    ssh.load_system_host_keys() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(hostname=hostname,username=username,password=password,port=int(port)) 
    stdin1,stdout1,stderr1=ssh.exec_command(cmd,timeout=10)
    print stdout1.read()
    ssh.close()

def install(request):
  try:
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
    obj=models.iplist(ip=ip,port=port,buffer=buffer,ver=version)
    obj.save()
    auth=models.ipauth(ip=lip,port=lport,username=lusername,password=lpassword)
    auth.save()
    return render_to_response('db/dbDetail.html',{'key':"mysql install suceess!"})

  except:
    obj=models.iplist(ip=ip,port=port,buffer=buff,ver=version)
    obj.save()
    auth=models.ipauth(ip=lip,port=lport,username=lusername,password=lpassword)
    auth.save()
    return render_to_response('db/dbDetail.html',{'key':"mysql install suceess!"})

def Model(request):
    iplist=models.iplist.objects.all()
    return render_to_response('db/Model.html',{'names':iplist})      

def backup(request):
    iplist=models.iplist.objects.all()
    backinfo=models.backup.objects.all()
    return render_to_response('db/backup.html',{'names':iplist,'bkinfo':backinfo})


def autobackup(request):
    postData = request.POST
    lip = postData.get('select1')
    t=ipauth.objects.get(ip=lip)

    now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  
    bk_name="all_%s.sql"%now
    
    cmd="/usr/local/mysql/bin/mysqldump -S /tmp/mysql3307.sock -A --single-transaction --master-data=2 >/tmp/all_%s.sql"%now
    sshlogin(t.ip,t.username,t.password,t.port,cmd)    
    
    bk=models.backup(ip=lip,bkname=bk_name,bktime=now)
    bk.save()
    backinfo=models.backup.objects.all()
    iplist=models.iplist.objects.all()  

    return render_to_response('db/backup.html',{'key':"mysql backup suceess!",'bkinfo':backinfo,'names':iplist})


