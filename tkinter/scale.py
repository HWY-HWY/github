"""
scale 控件，可以通过拖拽指示器来改变变量的值，类似音量的控制
"""


import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# from_ 指定起始值，to指定结束值 orient指定方向，HORIZONTAL水平，
# VERTICAL垂直
scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=10, length=200)
scale.set(10)
print(scale.get())
scale.pack()
win.mainloop()
