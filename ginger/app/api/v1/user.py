# -*- coding:utf-8 -*-
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

__author__ = 'MiracleWong'

api = Redprint('user')


@api.route('', methods=["GET"])
@auth.login_required
def get_user():
    return 'get user'


@api.route('', methods=["POST"])
def create_user():
    return 'get user'
