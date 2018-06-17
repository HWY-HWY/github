"""
Flask基础
"""

# 导入config配置文件中的内容
from config import DEBUG
from flask import Flask

# 创建一个Flask应用
app = Flask(__name__)
# 通过app.config.from_object这个方法去加载配置文件，其中的参数是配置文件的路径
# 返回的结果是一个字典。其中包括一个默认key DEBUG，其value为FALSE
# 需要注意的是：config这个方法的key只能是大写，不能是小写
app.config.from_object("config")
print(app.config["DEBUG"])

# 创建路由方法1，/hello和/hello/是通过重定向实现的
# 其实app.route 也是调用了add_url_rule
# @app.route("/hello/")


# 创建对应的路由所执行的视图函数
def hello():
    return "hello Flask, hello python"


def hwy():
    return "this is home page"


# 创建路由方法2：通过绑定路由与视图函数实现
# 参数1：路由，参数2：视图函数
app.add_url_rule('/hello', view_func=hello)
app.add_url_rule("/index", view_func=hwy)


# 判断是否是直接通过该函数来加载开启服务器，
# 如果不是，则不会执行run方法，因为通常在生产环境下，都是通过如nginx等
# 方法去部署服务器，所以不会通过run来启动服务器，而是通过nginx来开启，
# 如果同时开启了多个服务器，这是不允许的，所以需要通过if来判断
if __name__ == "__main__":
    # 运行Flask应用，并开启调试模式
    # 0.0.0.0是让可以通过其他的服务器来访问
    app.run(host="0.0.0.0",debug=DEBUG)