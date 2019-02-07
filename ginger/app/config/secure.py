# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''
import os

__author__ = 'MiracleWong'

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/ginger'
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True