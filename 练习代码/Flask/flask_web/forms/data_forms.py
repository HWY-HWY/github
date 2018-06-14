# -*- coding: utf-8 -*-
# @File  : data_forms.py
# @Author: 一稚杨
# @Date  : 2018/6/9/009
# @Desc  : 利用wtforms进行参数验证
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


# 定义一个参数验证类，该类继承于Form这个类方法
class data_forms(Form):
    name = StringField(validators=[DataRequired() ,Length(min=1, max=20)])
    age = IntegerField(validators=[NumberRange(min=1, max=100, message="不在正常年龄范围")], default=18)