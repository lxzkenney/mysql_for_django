from django.db import models

class UserInfo(models.Model):
    Nid = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=256)
    RealName =  models.CharField(max_length=256)
    Email = models.EmailField(max_length=256)
    

class iplist(models.Model):
    class Meta:
        db_table = 'iplist'
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=32)
    port = models.CharField(max_length=32)
    ver =  models.CharField(max_length=32)
    buffer = models.CharField(max_length=32)
    
#lost alter table backup change bktime bktime datetime default CURRENT_TIMESTAMP;  
class backup(models.Model):
    class Meta:
        db_table = 'backup'
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=32)
    bktime = models.DateTimeField();
    bkname = models.CharField(max_length=64)


class ipauth(models.Model):
    class Meta:
        db_table = 'ipauth'
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=32)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    port = models.CharField(max_length=12)
    extra = models.CharField(max_length=255)


