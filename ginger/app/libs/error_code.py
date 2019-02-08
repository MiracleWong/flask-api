# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''
from app.libs.error import APIException

__author__ = 'MiracleWong'


class Success(APIException):
    code = 201
    error_code = 0
    msg = "ok"


class ClientTypeError(APIException):
    code = 400
    error_code = 1006
    msg = "Client is invalid"


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = "Invalid Parameter"
