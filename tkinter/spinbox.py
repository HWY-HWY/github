"""
数值范围控件，可以通过操作改变数值
"""

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")


def updata():
    print(v.get())


v = tkinter.StringVar()
# from_ 指定起始值，to指定结束值,increment相当于指定分辨率，
# value 指定显示的值，一般不与上面的参数同时使用
spinbox = tkinter.Spinbox(win, from_=0, to=10, increment=2, textvariable=v, command=updata)
v.set(4)
spinbox.pack()
win.mainloop()
