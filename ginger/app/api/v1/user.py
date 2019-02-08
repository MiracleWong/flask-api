# -*- coding:utf-8 -*-
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.modules.user import User

__author__ = 'MiracleWong'

api = Redprint('user')


@api.route('', methods=["GET"])
@auth.login_required
def get_user():
    user = User.query.get_or_404()
    return 'I am MiracleWong'


@api.route('', methods=["POST"])
def create_user():
    return 'get user'
