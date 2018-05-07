"""
下拉控件
"""

import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("hwy")
win.geometry('400x400')
# 创建下拉菜单
com = ttk.Combobox(win)
# 设置下拉值
com["value"] = ("python", "C++", "java")
# 设置初始值
com.current(0)
com.pack()


def showinfo(event):
    print(com.get())


# 绑定事件，该事件在下拉之发生变化时触发
com.bind("<<ComboboxSelected>>", showinfo)
win.mainloop()
