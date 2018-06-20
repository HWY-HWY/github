"""
创建app并初始化
"""

from flask import Flask
from settings import config


def create_app():
    # 在创建核心应用是指出静态文件和模板文件的位置，即为app指定了寻找的路径其中 template_folder指定
    # 模板文件的路径， static_folder指定静态文件的路径，还可以使用static_path_url指定加载静态文件的url
    app = Flask(__name__, template_folder='../blueprint1/templates', static_folder='../blueprint1/static')
    app.config.from_object(config)
    # 注册蓝图
    print("~~~~~~~~~~~~~~~")
    print(__name__)
    print("~~~~~~~~~~~~~~~")
    register_blueprint(app)
    return app


def register_blueprint(app):
    from blueprint1.views1 import blueprint1
    app.register_blueprint(blueprint1)

