# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/9
"""

__author__ = 'MiracleWong'


class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    allow_api = ['v1.get_user']


def is_in_scope(scope, endpoint):
    # 如何通过类的名字拿到类的对象，这就是类的反射
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False

