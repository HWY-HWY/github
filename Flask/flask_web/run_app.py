# -*- coding: utf-8 -*-
# @File  : run_app.py
# @Author: 一稚杨
# @Date  : 2018/6/8/008
# @Desc  : 引入create_app方法创建一个app并运行
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\Flask')
from flask_web import create_app
from flask import request, render_template

app = create_app()


@app.route("/CSS")
def CSS():
    return render_template("CSS背景.html")


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=8000)
