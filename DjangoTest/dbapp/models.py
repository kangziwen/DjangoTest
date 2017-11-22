from django.db import models

# Create your models here.
'''
 根据类自动创建数据库表
# app下的models.py	 建表
    python manage.py makemigrations
    python manage.py  migrate
'''
from django.db import models

# 用户表
class UserInfo(models.Model):
    # 默认创建自增长id主键
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=60)

