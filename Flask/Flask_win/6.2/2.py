# -*- coding: utf-8 -*-
# @File  : 2.py
# @Author: 一稚杨
# @Date  : 2018/6/2/002
# @Desc  : 利用url传递参数

from flask import Flask

# 创建一个flask应用
app = Flask(__name__)


# 指定路由并对应一个视图函数,通过<data>来传递数据
@app.route("/index/<username>")
def index_page(username):
    # 要提取出url中的参数，只需要用对应的参数名即可，但是需要在对应的视图函数中传入该变量名
    username = username
    return "hell ipad, i am windows %s" % username

# 启动应用
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
