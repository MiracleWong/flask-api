# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/7
"""

from app.libs.error import APIException

__author__ = 'MiracleWong'


class Success(APIException):
    code = 201
    error_code = 0
    msg = "ok"


class DeleteSuccess(Success):
    code = 202
    error_code = -1


class ServerError(APIException):
    code = 500
    error_code = 999
    msg = "Sorry, we made a mistake"


class ClientTypeError(APIException):
    code = 400
    error_code = 1006
    msg = "Client is invalid"


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = "Invalid Parameter"


class NotFound(APIException):
    code = 404
    error_code = 1001
    msg = "The resource are not found "


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = "Authorization Failed"
