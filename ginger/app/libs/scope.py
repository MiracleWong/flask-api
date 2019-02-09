# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/9
"""

__author__ = 'MiracleWong'


class Scope:

    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
        return self


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']

    def __init__(self):
        self.add(UserScope())
        print(self.allow_api)


class UserScope(Scope):
    allow_api = ['v1.A']


class SuperScope(Scope):
    allow_api = ['v1.C']

    def __init__(self):
        self.add(UserScope()).add(AdminScope())
        print(self.allow_api)


SuperScope()
AdminScope()


def is_in_scope(scope, endpoint):
    # 如何通过类的名字拿到类的对象，这就是类的反射
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False

