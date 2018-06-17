# -*- coding: utf-8 -*-
# @File  : views1.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 创建一个模型类

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

# 实例化一个SQLAlchemy
db = SQLAlchemy()


# 创建一个模型类，需要继承于db.Model
class book(db.Model):
    # 创建对应的数据字段，并指定类型
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    # default表示当对应的数据为空时，默认设置为default的值, unique设置该字段为唯一的
    author = Column(String(20), default="一稚杨", unique=True)