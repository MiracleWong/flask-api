# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''

__author__ = 'MiracleWong'


from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.modules.user import User


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(
        min=5, max=20
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

    # def __register_user_by_email(form):
    #     User.register_by_email(form.account.data,form.secret.data)


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[
        DataRequired(), length(min=2, max=22)
    ])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValueError