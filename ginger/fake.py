# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/9
"""

__author__ = 'MiracleWong'

from app import create_app
from app.modules.base import db
from app.modules.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)