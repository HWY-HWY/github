'''
按钮控件
'''


import tkinter


def button():
    print('hwy is a good man')


win = tkinter.Tk()
win.title('黄文杨')
win.geometry('400x400+400+200')
button = tkinter.Button(win, text="按钮", command=button, width=5, height=5)
button2 = tkinter.Button(win, text="quit", command=win.quit,)
button.pack()
button2.pack()
win.mainloop()
