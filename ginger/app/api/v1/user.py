# -*- coding:utf-8 -*-
from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.modules.user import User

__author__ = 'MiracleWong'

api = Redprint('user')


# class QiYue(object):
#     name = 'qiyue'
#     age = 18
#
#     def __init__(self):
#         self.gender = 'male'
#
#     def keys(self):
#         return ['name', 'age', 'gender']
#
#     def __getitem__(self, item):
#         return getattr(self, item)


@api.route('/<int:uid>', methods=["GET"])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)

    return jsonify(user)


@api.route('', methods=["POST"])
def create_user():
    return 'get user'
