# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/9
"""

__author__ = 'MiracleWong'


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        # 运算符重载
        return self


class UserScope(Scope):
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']
    allow_module = []


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        # self + UserScope()
        print(self.allow_api)


def is_in_scope(scope, endpoint):
    # 如何通过类的名字拿到类的对象，这就是类的反射
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False

