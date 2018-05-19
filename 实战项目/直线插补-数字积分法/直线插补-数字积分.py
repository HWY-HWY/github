"""
数字积分法--直线插补
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
def runin(xo, yo, k, p, max_num, jrx, jry, xe, ye):
    # 斜率大于等于零
    if k >= 0:
        # 终点在第一象限
        if float(entry2.get()) >= 0:
            # print(jrx, jry, max_num)
            jrx = jrx + xe
            jry = jry + ye
            if jrx >= 2**max_num:
                xo = xo + p
                jrx = jrx - 2**max_num
            if jry >= 2**max_num:
                yo = yo + p
                jry = jry - 2**max_num
        # 终点在第三象限
        else:
            jrx = jrx + abs(xe)
            jry = jry + abs(ye)
            if jrx >= 2**max_num:
                xo = xo - p
                jrx = jrx - 2**max_num
            if jry >= 2**max_num:
                yo = yo - p
                jry = jry - 2**max_num
        result = (xo, yo, jrx, jry)
        return result
    # 斜率小于零
    else:
        # 终点在第四象限
        if float(entry2.get()) >= 0:
            jrx = jrx + abs(xe)
            jry = jry + abs(ye)
            if jrx >= 2**max_num:
                xo = xo + p
                jrx = jrx - 2**max_num
            if jry >= 2**max_num:
                yo = yo - p
                jry = jry - 2**max_num
        # 终点在第二象限
        else:
            jrx = jrx + abs(xe)
            jry = jry + abs(ye)
            if jrx >= 2**max_num:
                xo = xo - p
                jrx = jrx - 2**max_num
            if jry >= 2**max_num:
                yo = yo + p
                jry = jry - 2**max_num
        result = (xo, yo, jrx, jry)
        return result


# 得到累加器的位数
def get_digit(max_num):
    i = 1
    while(1):
        if 2**i >= max_num:
            break
        i = i + 1
    return i


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
    max_num = max(abs(xe - xo), abs(ye - yo))
    digit = get_digit(max_num)
    result1 = function(x, y)
    k = result1[0]
    # b = result1[1]
    plt.axis("equal")
    plt.plot(x, y)
    mode = R1.get()
    txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")
    if mode == 11:
        jrx = 0
        jry = 0
        number = int((2**digit)/p)
    elif mode == 22:
        jrx = (2**digit)/2
        jry = (2**digit)/2
        number = int((2**digit)/p)
    elif mode == 33:
        jrx = 2**digit
        jry = 2**digit
        number = int((2**digit)/p - 1)
    xe = xe - xo
    ye = ye - yo
    for i in range(number):
        # print(xo, yo)
        # print(result3)
        result2 = runin(xo, yo, k, p, digit, jrx, jry, xe, ye)  # 终点
        plot_end = result2
        plt.pause(0.5)
        plt.plot((xo, plot_end[0]), (yo, plot_end[1]))
        xo = plot_end[0]
        yo = plot_end[1]
        jrx = plot_end[2]
        jry = plot_end[3]
        txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")
    plt.show()


# 清除数据
def clear():
    txt.delete(0.0, tkinter.END)


win = tkinter.Tk()
win.title("hwy")
win.geometry("600x400")
win.resizable(width=False, height=False)
label1 = tkinter.Label(win, text="直线插补--数字积分法")
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
R1 = tkinter.IntVar()
radio3 = tkinter.Radiobutton(win, text="不加载", value=11, variable=R1)
radio3.place(x=100, y=280)
radio4 = tkinter.Radiobutton(win, text="半加载", value=22, variable=R1)
radio4.place(x=200, y=280)
radio4 = tkinter.Radiobutton(win, text="全加载", value=33, variable=R1)
radio4.place(x=300, y=280)
R1.set(11)
win.mainloop()
