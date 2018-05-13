"""
逐点比较法--直线插补
"""
# -- coding:utf-8 --
import matplotlib.pyplot as plt
import tkinter


# 定义直线函数
def function(x, y):
    xo = x[0]
    xe = x[1]
    yo = y[0]
    ye = y[1]
    # 得到斜率
    k = (ye - yo)/(xe - xo)
    # 得到b
    b = ye - k*xe
    return (k, b)


def is_ok(xo, yo, k, b):
    num = k*xo + b - yo
    # 设置精度
    a = int(entry5.get())
    num = round(num, a)
    if k >= 0:
        if float(entry2.get()) >= 0:
            if num <= 0:
                return 1
            else:
                return 0
        else:
            if num >= 0:
                return 1
            else:
                return 0
    else:
        if float(entry2.get()) >= 0:
            if num >= 0:
                return 1
            else:
                return 0
        else:
            if num <= 0:
                return 1
            else:
                return 0


# 插补函数
def runin(result, xo, yo, k, p):
    if k >= 0:
        if result == 1:
            if float(entry2.get()) >= 0:
                xo = xo + p
                yo = yo
            else:
                xo = xo - p
                yo = yo
        else:
            if float(entry2.get()) >= 0:
                yo = yo + p
                xo = xo
            else:
                yo = yo - p
                xo = xo
        result = (xo, yo)
        return result
    else:
        if result == 1:
            if float(entry2.get()) >= 0:
                xo = xo + p
                yo = yo
            else:
                xo = xo - p
                yo = yo
        else:
            if float(entry2.get()) >= 0:
                yo = yo - p
                xo = xo
            else:
                yo = yo + p
                xo = xo
        result = (xo, yo)
        return result


# 画出图形
def show():
    plt.figure()
    plt.title(u"line")
    # print("起点：" + "\n")
    xo = float(entry.get())
    yo = float(entry1.get())
    # print("终点" + "\n")
    xe = float(entry2.get())
    ye = float(entry3.get())
    p = float(entry4.get())
    x = (xo, xe)
    y = (yo, ye)
    result1 = function(x, y)
    k = result1[0]
    b = result1[1]
    number = int(abs(xe - xo) + abs(ye - yo))
    plt.axis("equal")
    plt.plot(x, y)
    txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")
    for i in range(int(number/p)):
        # print(i)
        # print(xo, yo)
        result3 = is_ok(xo, yo, k, b)
        # print(result3)
        result2 = runin(result3, xo, yo, k, p)  # 终点
        plot_end = result2
        plt.pause(0.5)
        plt.plot((xo, plot_end[0]), (yo, plot_end[1]))
        xo = plot_end[0]
        yo = plot_end[1]
        txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")
    plt.show()


# 清除数据
def clear():
    txt.delete(0.0, tkinter.END)


win = tkinter.Tk()
win.title("hwy")
win.geometry("600x400")
win.resizable(width=False, height=False)
label1 = tkinter.Label(win, text="直线插补")
label1.pack()
label2 = tkinter.Label(win, text="起点坐标：Xo=")
label2.place(x=100, y=100)
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
e.set(0)
entry.place(x=200, y=100)
label3 = tkinter.Label(win, text="起点坐标：Yo=")
label3.place(x=100, y=130)
e1 = tkinter.Variable()
entry1 = tkinter.Entry(win, textvariable=e1)
e1.set(0)
entry1.place(x=200, y=130)

label4 = tkinter.Label(win, text="终点坐标：Xe=")
label4.place(x=100, y=160)
e2 = tkinter.Variable()
entry2 = tkinter.Entry(win, textvariable=e2)
e2.set(10)
entry2.place(x=200, y=160)

label5 = tkinter.Label(win, text="终点坐标：Ye=")
label5.place(x=100, y=190)
e3 = tkinter.Variable()
entry3 = tkinter.Entry(win, textvariable=e3)
e3.set(10)
entry3.place(x=200, y=190)

label6 = tkinter.Label(win, text="脉冲当量：P=")
label6.place(x=100, y=220)
e4 = tkinter.Variable()
entry4 = tkinter.Entry(win, textvariable=e4)
e4.set(1)
entry4.place(x=200, y=220)

label7 = tkinter.Label(win, text="精度：A=")
label7.place(x=100, y=250)
e5 = tkinter.Variable()
entry5 = tkinter.Entry(win, textvariable=e5)
e5.set(5)
entry5.place(x=200, y=250)

# 显示坐标值
txt = tkinter.Text(win)
txt.place(x=400, y=30)

button = tkinter.Button(win, text="插补计算", command=show)
button.place(x=250, y=350)
button1 = tkinter.Button(win, text="清除坐标", command=clear)
button1.place(x=340, y=350)
win.mainloop()
