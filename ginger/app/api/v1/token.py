# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/8
'''
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.modules.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

__author__ = 'MiracleWong'

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_MAIL: User.verify,
    }
    print(form.type.data)
    print(ClientTypeEnum(form.type.data))
    print("form.account.data")
    print(form.account.data)
    print("form.secret.data")
    print(form.secret.data)
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    print("expiration")
    print(expiration)
    token = generate_auth_token(identity['uid'], form.type.data,
                                None, expiration)
    print("token")
    print(token)
    t = {
        'token': token.decode("ascii")
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
    })