# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/9
"""

__author__ = 'MiracleWong'


class AdminScope:
    allow_api = ['super_get_user']


class UserScope:
    allow_api = ['super_get_user']


def is_in_scope(scope, endpoint):
    if endpoint in scope.allow_api:
        return True
    else:
        return False

