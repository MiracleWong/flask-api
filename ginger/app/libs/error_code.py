# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''
from werkzeug.exceptions import HTTPException
from app.libs.error import APIException

__author__ = 'MiracleWong'


class ClientTypeError(APIException):
    code = 400
    error_code = 1006
    msg = "Client is invalid"
    

