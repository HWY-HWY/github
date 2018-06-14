# -*- coding: utf-8 -*-
# @File  : 重定向.py
# @Author: 一稚杨
# @Date  : 2018/6/7/007
# @Desc  : 重定向和404页面定义

# redirect实现重定向
from flask import Flask, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = '123456'


@app.route("/index1")
def index1():
    flash("登录成功", category="login")
    flash("hello",category="hello")
    return redirect("/index2/")


@app.route("/index2/")
def index2():
    return render_template("flash.html")


@app.errorhandler(404)
def error(error):
    return render_template("404.html"),404


# form表单action为空时访问那个页面？结论：当action为空时，数据提交给发送数据的页面
@app.route("/action_none", methods=["GET", "POST"])
def action_none():
    return render_template("action.html")


app.run(debug=True)