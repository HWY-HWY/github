# -*- coding: utf-8 -*-
# @File  : views2.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 蓝图2

from flask import Blueprint

# 实例化一个蓝图对象
blueprint2 = Blueprint("blueprint3", __name__)


# 通过blueprint2来创建路由
@blueprint2.route("/index2")
def index2():
    return "blueprint2"
