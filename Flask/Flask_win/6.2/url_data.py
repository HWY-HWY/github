"""
通过url传递参数
"""

from flask import Flask


# 创建一个Flask应用
app = Flask(__name__)

# 创建视图函数
def index(data1, data2):
    return "this is Flask" + data1 + data2


# 创建路由映射
app.add_url_rule("/index/<data1>/<data2>", view_func=index)


# 开启Flask应用
if __name__ == "__main__":
    app.run(debug=True)

