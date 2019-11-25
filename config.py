# encoding: utf-8
DEBUG = True
'''
The SQLALCHEMY_DATABASE_URI is used to configure your mysql database
root and 123456 is my database user and password, you need replace them with yours
'''
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@db:3306/demo?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
