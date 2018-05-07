'''
单选框控件
'''

import tkinter


win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")


def showinfo():
    print(r.get())


r = tkinter.IntVar()
redio1 = tkinter.Radiobutton(win, text="one", value=11, variable=r, command=showinfo)
redio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=22, variable=r, command=showinfo)
radio2.pack()
win.mainloop()
