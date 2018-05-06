"""
点击按钮显示输入框的内容
"""


import tkinter


def showinfo():
    print(entry.get())


win = tkinter.Tk()
win.title('python')
win.geometry("400x400+400+200")
entry = tkinter.Entry(win, show="#")
entry.pack()
button = tkinter.Button(win, text="按钮", command=showinfo)
button.pack()
button2 = tkinter.Button(win, text="quit", command=win.quit)
button2.pack()
win.mainloop()
