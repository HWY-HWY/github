"""
视图函数1，继承于蓝图1
"""

from flask import Blueprint, render_template

# 实例化一个蓝图
blueprint1 = Blueprint('blueprint1', __name__)


# 利用blueprint1来创建视图函数
@blueprint1.route('/index/')
def index():
    return "this is blueprint1"


@blueprint1.route('/index2/')
def index2():
    return render_template('index2.html')
