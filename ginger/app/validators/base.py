# -*- coding:utf-8 -*-
"""
created by MiracleWong on 2019/2/8
"""

from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException

__author__ = 'MiracleWong'


class BaseForm(Form):
    def __init__(self):
        data = request.json
        print(data)
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        print("valid:")
        print(valid)
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
