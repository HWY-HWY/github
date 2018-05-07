'''
鼠标点击事件
'''

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
button = tkinter.Button(win, text="button")


def showinfo(event):
    print(event.x, event.y)


# 绑定事件
button.bind("<Button-2>", showinfo)
button.pack()
win.mainloop()
