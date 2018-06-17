# -*- coding: utf-8 -*-
# @File  : __init__.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 初始化，创建一个共享蓝图

from flask import Blueprint

blueprint = Blueprint("web", __name__)

from . import views1, views2
