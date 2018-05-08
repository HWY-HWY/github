"""
tkinter 实现ug外挂安装
"""
#coding:utf-8
import tkinter
from tkinter.filedialog import askdirectory
import webbrowser
import os
import re
import sys

win = tkinter.Tk()
win.title("ug插件安装器")
win.geometry("400x200")
win.iconbitmap("C:\\Users\\Administrator\\Desktop\\个人博客\\nx.ico")


# 选择路径函数
def filepath1():
    path_ = askdirectory()
    path1.set(path_)


def filepath2():
    path_ = askdirectory()
    path2.set(path_)


def showinfo():
    path = entry1.get()
    newpath = os.path.join(path, "UGII\\menus\\custom_dirs.dat")
    # 获得当前绝对路径
    abspath = sys.path[0]
    # 以追加模式打开
    with open(newpath, "a", encoding='gbk') as f:
        f.write(abspath + "\n")
    # 修改源程序的路径
    path1 = os.path.join(abspath + "\\startup\\muyuyu.tbr")
    with open(path1, "r", encoding='gbk') as f:
        lines = f.readlines()
    with open(path1, "w") as f_w:
        for line in lines:
            str1 = re.findall("BITMAP   (.*)icon", line)
            str2 = re.findall("ACTION   (.*)startup", line)
            if str1:
                line = line.replace(str1[0], abspath + "\\")
            if str2:
                line = line.replace(str2[0], abspath + "\\")
            f_w.write(line)


def gourl(event):
    webbrowser.open("www.huangwenyang.cn")


path1 = tkinter.StringVar()
path2 = tkinter.StringVar()
# 标题栏
label1 = tkinter.Label(text="欢迎使用ug插件安装器--hwy")
label1.pack()
# 设置ug选择路径
label2 = tkinter.Label(text="请选择ug安装路径：")
label2.place(x=10, y=50)
entry1 = tkinter.Entry(textvariable=path1)
entry1.place(x=125, y=50)
button1 = tkinter.Button(text="选择路径", command=filepath1)
button1.place(x=280, y=45)
# 操作按钮
button4 = tkinter.Button(text="确定", command=showinfo)
button4.place(x=350, y=160)
button5 = tkinter.Button(text="退出", command=win.quit)
button5.place(x=300, y=160)
# 提示
label3 = tkinter.Label(text="提示：该软件应与startup同目录")
label3.place(x=110, y=110)
label4 = tkinter.Label(text="欢迎访问我的个人网站：www.huangwenyang.cn")
# 绑定事件
label4.bind("<Button-1>", gourl)
label4.place(x=70, y=130)
win.mainloop()
