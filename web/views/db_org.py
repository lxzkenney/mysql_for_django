from django.shortcuts import render, render_to_response
from django.http  import HttpResponse
import json
import MySQLdb
import sys,datetime,time
import paramiko
from web import models


def manage(request):
    return render_to_response('Home/manage.html')



def install(request):
  try:
      
    postData = request.POST
    ip = postData.get('ip')
    version = postData.get('version')    
    port = postData.get('port')   
    buffer = postData.get('buffer')
  
    version = version.encode("utf-8")
    ip = ip.encode("utf-8")
    port = port.encode("utf-8")
    buffer = buffer.encode("utf-8")

    host='10.10.203.94' 
    name='root' 
    password='e_OP' 

    ssh=paramiko.SSHClient() 
    ssh.load_system_host_keys() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(hostname=host,username=name,password=password) 
    stdin1,stdout1,stderr1=ssh.exec_command("sh /opt/software/mysql_install.sh -v%s -p%s -s%s" %(version,port,buffer),timeout=10)
    print stdout1.read()
    ssh.close()

    obj=models.iplist(ip=ip,port=port,buffer=buffer,ver=version)
    obj.save()
    return render_to_response('db/dbDetail.html',{'key':"mysql install suceess!"})

  except:
    obj=models.iplist(ip=ip,port=port,buffer=buffer,ver=version)
    obj.save()
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
    ip = postData.get('select1')
    host='192.168.39.210' 
    name='root' 
    password='123456'
   # now = datetime.datetime.now()
    now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  
#    nowf=now.strftime('%Y-%m-%d_%H:%M:%S') 
    nowf=time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime()) 
    
    print nowf
    
    ssh=paramiko.SSHClient() 
    ssh.load_system_host_keys() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(hostname=host,username=name,password=password) 
    stdin1,stdout1,stderr1=ssh.exec_command("/usr/local/mysql/bin/mysqldump -S /tmp/mysql3307.sock -A --single-transaction --master-data=2 >/tmp/all_%s.sql"%nowf,timeout=10)
    print stdout1.read()

    bk_name="all_%s.sql"%nowf
    print bk_name
    bk=models.backup(ip=ip,bkname=bk_name,bktime=now)
    bk.save()
    backinfo=models.backup.objects.all()
    ssh.close()
    return render_to_response('db/backup.html',{'key':"mysql backup suceess!",'bkinfo':backinfo})


    
    
    
    
    
    
    
    
    

  

