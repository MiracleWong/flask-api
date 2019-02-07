# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''
from app.libs.redprint import Redprint

__author__ = 'MiracleWong'

api = Redprint('client')


@api.route('/register', methods=["GET"])
def sign_up():
    pass