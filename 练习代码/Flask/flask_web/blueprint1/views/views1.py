# -*- coding: utf-8 -*-
# @File  : views1.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 创建另一个视图函数，与views共享一个蓝图

from . import blueprint
from flask import render_template


@blueprint.route("/index3")
def index3():
    return render_template("data_get.html")
