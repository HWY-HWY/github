"""
Flask Response对象的使用
"""
from flask import Flask, make_response

# 创建一个Flask应用
app = Flask(__name__)


# 创建一个视图函数
def index():
    # 其实return的实质是：将返回的内容交给response这个类去处理
    # 最终返回的是response实例化的一个对象，其中有一些参数
    # 比如status code（状态码），content type（返回内容的类型）
    # 由于返回给前端的内容实质就是response实例化过后的对象，所以我们可以修改response
    # 中的内容来控制返回的内容

    # 创建headers
    headers = {
        "Content-Type": "text/plain",
        "data": "this is Flask",
    }

    # 创建Response对象，并指定参数，参数1：返回的内容，参数2：状态码(301表示重定向)
    Response = make_response("<html>this is Flask</html>", 200)
    # 修改Response对象的headers
    Response.headers = headers
    return Response


# 创建路由映射表
app.add_url_rule("/index/", view_func=index)


# 开启应用
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
