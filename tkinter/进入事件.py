"""
进入事件
"""

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
label = tkinter.Label(win, text="python")
label.pack()


def showinfo(event):
    print("------")


label.bind("<Enter>", showinfo)
win.mainloop()
