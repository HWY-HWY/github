"""
表格布局
"""


import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# 创建三个标签
label1 = tkinter.Label(win, text="python", bg="blue")
label2 = tkinter.Label(win, text="java", bg="red")
label3 = tkinter.Label(win, text="C++", bg="pink")
# 指定控件所在的行和列
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=1)
win.mainloop()
