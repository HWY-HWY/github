# -*- coding: utf-8 -*-
# @File  : POST_data.py.py
# @Author: 一稚杨
# @Date  : 2018/6/7/007
# @Desc  : 利用post进行数据交互和文件的上传

from flask import Flask, render_template, request, make_response
import os

# 设置文件上传存放的文件夹
FOLDER = "static/uploads"

# 创建一个flask应用
app = Flask(__name__)
# 设置文件的下载路径
app.config["UPLOAD_FOLDER"] = FOLDER


# 创建路由并指定视图函数
@app.route("/post")
def post():
    # 通过make——response设置cookie
    res = make_response(render_template("post.html"))
    # 第一个参数对应于cookie中的key，第二个参数对应于value
    res.set_cookie("name", "hwy")
    res.set_cookie("age", '22')
    return res


@app.route("/get_data/", methods=["GET", "POST"])
def get_data():
    # 得到post提交的数据
    if request.method == "GET":
        data = request.args.get("username")
    # 得到请求的方法
    method = request.method
    # 得到cookie
    data = request.form
    cookie = request.cookies
    print(data)
    return render_template("get_data.html", data=data)


# 提交文件
@app.route("/file")
def file():
    return render_template("file.html")


# 对提交的文件进行处理
@app.route("/get_filename/", methods=["GET", "POST"])
def filename():
    # 验证密码是否正确
    password = request.form["password"]
    if password == "muyuyu123":
        # 验证是否选择了文件
        x = request.files.to_dict()
        if x == {}:
            result = "请选择文件"
        else:
            # 得到文件
            for file in request.files.getlist("filename[]"):
                # 得到文件名
                filename = file.filename
                # 将文件保存到本地
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = "上传成功"
    else:
        result = "密码错误"
    return result

# 运行app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="80")