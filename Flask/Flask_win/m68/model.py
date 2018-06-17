# -*- coding: utf-8 -*-
# @File  : model.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 使用模型类

from flask import Flask
from m68.models.books import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://一稚杨:muyuyu123@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 关联app与db对象
db.init_app(app)
db.create_all(app=app)


@app.route("/index")
def index():
    return "model"


if __name__ == "__main__":
    app.run(debug=True)

