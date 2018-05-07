"""
相对布局
"""

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# 创建三个标签
label1 = tkinter.Label(win, text="python", bg="blue")
label2 = tkinter.Label(win, text="java", bg="red")
label3 = tkinter.Label(win, text="C++", bg="pink")
# fill=tkinter.Y 指定填充方法为Y，side=tkinter.RIGHT 指定放置的位置为靠右
label1.pack(fill=tkinter.Y, side=tkinter.RIGHT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()
win.mainloop()
