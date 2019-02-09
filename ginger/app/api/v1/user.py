# -*- coding:utf-8 -*-
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.modules.base import db
from app.modules.user import User

__author__ = 'MiracleWong'

api = Redprint('user')


@api.route('/<int:uid>', methods=["GET"])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=["GET"])
@auth.login_required
def get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=["DELETE"])
@auth.login_required
def delete_user():
    # g变量是线程隔离的。不会出现用户错乱的问题
    uid = g.user.uid

    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=["POST"])
def create_user():
    return 'get user'
