'''
		Django默认使用MySQLdb模块链接MySQL
		主动修改为pymysql，在project同名文件夹下的__init__文件中添加如下代码即可：
'''
'''
		django-admin startproject mysite
		python manage.py startapp cmdb


'''
import pymysql
pymysql.install_as_MySQLdb()