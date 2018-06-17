# -*- coding: utf-8 -*-
# @File  : 3.py.py
# @Author: 一稚杨
# @Date  : 2018/6/4/004
# @Desc  : 静态文件的使用

from flask import Flask, render_template

# 创建一个flask应用
app = Flask(__name__)

# 指定路由并设置对应的视图函数
@app.route("/index")
def index():
    return render_template("index.html")

# 启动应用
if __name__ == "__main__":
    app.run(debug=True)
