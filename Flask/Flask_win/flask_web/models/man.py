# -*- coding: utf-8 -*-
# @File  : man.py
# @Author: 一稚杨
# @Date  : 2018/6/10/010
# @Desc  : 创建一个man模型类，用于与数据库进行交互

from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy


# 利用flask提供的SQLAlchemy类实例化一个类，实际就相当于创建一个
# 连接数据数据库的一个引擎，后面创建模型类时直接继承该类就可以自动与数据表相关联

db = SQLAlchemy()


class man(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    age = Column(Integer, default=18)

