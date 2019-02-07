# -*- coding:utf-8 -*-
'''
created by MiracleWong on 2019/2/7
'''
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum

__author__ = 'MiracleWong'


class ClientForm(Form):
    account = StringField(validators=[DataRequired, length(
        min=5, max=20
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
