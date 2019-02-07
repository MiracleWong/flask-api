# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''
from sqlalchemy import Integer, Column, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.modules.base import Base, db

__author__ = 'MiracleWong'


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24),unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 在一个对象的内部再次定义对象本身是不合适的，但是如果使用的是静态方法的话，就是正常的。
    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.password = secret
            user.email = account
            db.session.add(user)
