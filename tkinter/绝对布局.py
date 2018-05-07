"""
绝对布局
"""

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# 创建三个标签
label1 = tkinter.Label(win, text="python", bg="blue")
label2 = tkinter.Label(win, text="java", bg="red")
label3 = tkinter.Label(win, text="C++", bg="pink")
# 指定位置，距离x，y，的距离
label1.place(x=0, y=0)
label2.place(x=50, y=50)
label3.place(x=100, y=100)
win.mainloop()
