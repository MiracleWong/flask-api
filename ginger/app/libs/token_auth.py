# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/8
"""

from flask_httpauth import HTTPBasicAuth

__author__ = 'MiracleWong'


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, password):
    return "Hello World"