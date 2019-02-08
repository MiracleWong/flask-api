# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/8
"""

from collections import namedtuple
from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.error_code import AuthFailed

__author__ = 'MiracleWong'


auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        # token无法解密的异常
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        # token时间过期的异常
        raise AuthFailed(msg='token is expired', error_code=1003)

    uid = data['uid']
    ac_type = data['type']
    return User(uid, ac_type, '')

