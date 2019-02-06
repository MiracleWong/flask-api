# -*- coding:utf-8 -*-
from flask import Blueprint
from app.libs.redprint import Redprint
__author__ = 'MiracleWong'

# user = Blueprint('user', __name__)
api = Redprint('user')

@api.route('', methods=["GET"])
def get_user():
    return 'get user'\

@api.route('', methods=["POST"])
def create_user():
    return 'get user'