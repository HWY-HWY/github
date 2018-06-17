# -*- coding: utf-8 -*-
# @File  : 2.py
# @Author: 一稚杨
# @Date  : 2018/6/3/003
# @Desc  : 模板文件的使用
# 对于flask而言，模板文件的加载有两种情况，一种是使用模块，另一种是使用包
# 当你使用模板文件时，flask会自动到你的项目目录下的一个名为templates的文件中
# 去寻找指定的模板文件，所以所有的模板文件都应该放在templates这个文件夹中

from flask import Flask, render_template

# 创建一个flask应用

app = Flask(__name__)

# 创建路由并指定视图函数，通过加载静态模板来显示页面


@app.route("/index")
def index():
    # render_template 的第一个参数是模板文件，第二个参数是需要渲染的数据
    data = {"name": "一稚杨", "age": 20}
    return render_template("index.html", data=data)


# 运行app
if __name__ == "__main__":
    app.run(debug=True)
