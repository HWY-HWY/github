"""
指定按键事件
"""

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
label = tkinter.Label(win, text="python")
label.focus_set()
label.pack()


def showinfo(event):
    # 显示对应按键的字符
    print(event.char)
    # 显示对应按键的ascii码
    print(event.keycode)


label.bind("<a>", showinfo)
win.mainloop()
