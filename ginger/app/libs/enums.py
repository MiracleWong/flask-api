# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/7
"""

__author__ = 'MiracleWong'

from enum import Enum


class ClientTypeEnum(Enum):
    USER_MAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
