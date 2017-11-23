from django.db import models

# Create your models here.
'''
 根据类自动创建数据库表
# app下的models.py	 建表
    python3 manage.py makemigrations
    python3 manage.py  migrate
'''
from django.db import models
class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    # 创建时间
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    # 更新数据的时间 调用 m.save()方法才更新 update（）方法不更新时间
    uptime = models.DateTimeField(auto_now=True,null=True)
# 用户表
class UserInfo(models.Model):
    # 默认创建自增长id主键
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=60)
    12
    email = models.CharField(max_length=60,null=True)
    test = models.EmailField(max_length=30,null=True)

    user_group = models.ForeignKey('UserGroup',to_field='uid',null=True)
    user_type_choices = (
        (1,"超级用户"),
        (2,"普通用户"),
        (3,"普普通用户")
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)

