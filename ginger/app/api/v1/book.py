# -*- coding:utf-8 -*-
from app.libs.redprint import Redprint
__author__ = 'MiracleWong'

api = Redprint('book')


@api.route('', methods=["GET"])
def get_book():
    return 'get book'
