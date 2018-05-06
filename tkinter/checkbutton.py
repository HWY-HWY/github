'''
多选按钮
'''


import tkinter


win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")


def update():
    messge = ""
    if hobby1.get() == True:
        messge += "money\n"
    if hobby2.get() == True:
        messge += "power\n"
    if hobby3.get() == True:
        messge += "python\n"
    # 清空text中的内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, messge)


hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()
checkbutton1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=update)
checkbutton2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=update)
checkbutton3 = tkinter.Checkbutton(win, text="python", variable=hobby3, command=update)
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
text = tkinter.Text(win, width=40, height=5)
text.pack()
win.mainloop()
