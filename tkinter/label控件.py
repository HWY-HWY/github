"""
label: 标签控件，可以显示文本
"""


import tkinter

win = tkinter.Tk()
win.title('黄文杨')  # 设置标题
win.geometry('400x400+200+200')  # 设置大小和位置
# win选择父窗体 text 显示的文本内容 bg:背景色 fg：字体颜色
label = tkinter.Label(win, text="python",
bg="blue", fg="red", width=20, height=4, wraplength=40, justify="right",
anchor="s")
# 在窗口中显示出来控件
label.pack()
win.mainloop()
