# -*- coding:utf-8 -*-
from flask import Blueprint
from app.libs.redprint import Redprint
__author__ = 'MiracleWong'

# book = Blueprint('book', __name__)
api = Redprint('book')


@api.route('', methods=["GET"])
def get_book():
    return 'get book'
