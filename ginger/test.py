# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/8
"""

__author__ = 'MiracleWong'


class QiYue(object):
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ['name', 'age', 'gender']

    def __getitem__(self, item):
        return getattr(self, item)
