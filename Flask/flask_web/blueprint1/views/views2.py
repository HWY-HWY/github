# -*- coding: utf-8 -*-
# @File  : views2.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 利用蓝图（flask_web）机制分离视图函数与app应用
# 蓝图相当于一个中间机制，它可以间接联系app应用于视图函数，当我们将蓝图与app进行关联过后，这是关键
# 就可以通过蓝图来注册视图函数，而且还可以创建多个蓝图，每个蓝图对应不同的视图类别，而且每个蓝图可以
# 拥有不同的静态文件和模板

# from flask import Blueprint
#
# # 实例化一个蓝图对象
# # 第一个参数是蓝图的名称，第二个参数是蓝图所在的包或者模块，通常使用__name__
# blueprint1 = Blueprint("blueprint1", __name__)

# 这里不再使用单独创建一个蓝图，而是使用一个共享的蓝图，共享蓝图在__init__.py中定义
from . import blueprint
from flask import request, render_template
from flask_web.forms.data_forms import data_forms

# 通过blueprint这个实例化的蓝图对象来创建路由
@blueprint.route("/index/")
def index():
    # 实例化一个数据验证对象
    data_form = data_forms(request.args)
    # 启用验证
    if True:
        data = {"name": data_form.name.data.strip(), "age": data_form.age.data}
        return render_template("CSS背景.html", data=data)
    else:
        data = data_form.errors
        print(data)
        return "error"


