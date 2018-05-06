"""
输入控件
"""


import tkinter

win = tkinter.Tk()
win.title('黄文杨')  # 设置标题
win.geometry('400x400+200+200')  # 设置大小和位置
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
entry.pack()
e.set("hwy is a good man")  # 设置默认值
print(entry.get())   # 获取值
win.mainloop()
