"""
圆弧插补
"""

import numpy as np
import matplotlib.pyplot as plt
import tkinter


def show():
    # 得到对应的参数
    xo = float(entry.get())
    yo = float(entry1.get())
    xe = float(entry2.get())
    ye = float(entry3.get())
    x0 = float(entry4.get())
    y0 = float(entry5.get())
    mode = R1.get()
    r = ((xo - x0)**2 + (yo - y0)**2)**0.5
    # 计算圆弧对应的角度
    ag = angle(xo, yo, xe, ye, x0, y0, r)
    region(xo, yo, xe, ye, x0, y0, ag, r, mode)


# 计算圆弧对应的角度
def angle(xo, yo, xe, ye, x0, y0, r):
    c = ((xe - xo)**2 + (ye - yo)**2)
    ag = 1 - (c/(2 * r**2))
    return ag


# 划分象限区域
def region(xo, yo, xe, ye, x0, y0, ag, r, mode):
    r = r**2
    if mode == 22:
        # 逆圆插补
        # 圆弧起点和终点均在第一象限
        if xo >= x0 and yo >= y0 and xe >= x0 and ye >= y0 and xo >= xe:
            if xo == xe:
                x = np.linspace(xo, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 - r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 + r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, xe, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, x0, y0 + r**0.5, x0, y0, r, 1)
                runin(x0, y0 + r**0.5, x0 - r**0.5, y0, x0, y0, r, 2)
                runin(x0 - r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 3)
                runin(x0, y0 - r**0.5, x0 + r**0.5, y0, x0, y0, r, 4)
                runin(x0 + r**0.5, y0, xe, ye, x0, y0, r, 1)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)  # 这个表示在-5到5之间生成1000个x值
                # 对上述生成的1000个数循环用sigmoid公式求对应的y
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
                runin(xo, yo, xe, ye, x0, y0, r, 1)
                plt.show()
        # 起点在第一象限，终点在第二象限
        elif xo >= x0 and yo >= y0 and xe < x0 and ye >= y0 and xo > xe:
            x = np.linspace(xo, x0, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            x = np.linspace(x0, xe, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            runin(xo, yo, x0, y0 + r**0.5, x0, y0, r, 1)
            runin(x0, y0 + r**0.5, xe, ye, x0, y0, r, 2)
            plt.show()
        # 起点在第一象限，终点在第三象限
        elif xo >= x0 and yo >= y0 and xe < x0 and ye < y0 and xo > xe:
            x = np.linspace(xo, x0, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            x = np.linspace(x0, (x0 - r**0.5), 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            x = np.linspace((x0 - r**0.5), xe, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            runin(xo, yo, x0, y0 + r**0.5, x0, y0, r, 1)
            runin(x0, y0 + r**0.5, x0 - r**0.5, y0, x0, y0, r, 2)
            runin(x0 - r**0.5, y0, xe, ye, x0, y0, r, 3)
            plt.show()
        # 起点在第一象限，终点在第四象限
        elif xo >= x0 and yo >= y0 and xe > x0 and ye < y0 and yo > ye:
            x = np.linspace(xo, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, (x0 - r**0.5), 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace((x0 - r**0.5), x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0, y0 + r**0.5, x0, y0, r, 1)
            runin(x0, y0 + r**0.5, x0 - r**0.5, y0, x0, y0, r, 2)
            runin(x0 - r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 3)
            runin(x0, y0 - r**0.5, xe, ye, x0, y0, r, 4)
            plt.show()
        # 起点在第二象限，终点在第二象限
        elif xo <= x0 and yo >= y0 and xe <= x0 and ye >= y0 and xo >= xe:
            if xo == xe:
                x = np.linspace(xo, x0 - r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 + r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, xe, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, x0 - r**0.5, y0, x0, y0, r, 2)
                runin(x0 - r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 3)
                runin(x0, y0 - r**0.5, x0 + r**0.5, y0, x0, y0, r, 4)
                runin(x0 + r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 1)
                runin(x0, y0 + r**0.5, xe, ye, x0, y0, r, 2)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, xe, ye, x0, y0, r, 2)
                plt.show()
        # 起点在第二象限，终点在第三象限
        elif xo <= x0 and yo >= y0 and xe <= x0 and ye <= y0 and ye < yo:
            x = np.linspace(xo, x0 - r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0 - r**0.5, y0, x0, y0, r, 2)
            runin(x0 - r**0.5, y0, xe, ye, x0, y0, r, 3)
            plt.show()
        # 起点在第二象限，终点在第四象限
        elif xo <= x0 and yo >= y0 and xe >= x0 and ye <= y0 and xe > xo:
            x = np.linspace(xo, x0 - r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0 - r**0.5, y0, x0, y0, r, 2)
            runin(x0 - r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 3)
            runin(x0, y0 - r**0.5, xe, ye, x0, y0, r, 4)
            plt.show()
        # 起点在第二象限，终点在第一象限
        elif xo <= x0 and yo >= y0 and xe >= x0 and ye >= y0 and xe > xo:
            x = np.linspace(xo, x0 - r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 + r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0 - r**0.5, y0, x0, y0, r, 2)
            runin(x0 - r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 3)
            runin(x0, y0 - r**0.5, x0 + r**0.5, y0, x0, y0, r, 4)
            runin(x0 + r**0.5, y0, xe, ye, x0, y0, r, 1)
            plt.show()
        # 起点和终点在三象限
        elif xo <= x0 and yo <= y0 and xe <= x0 and ye <= y0 and xe >= xo:
            if xe == xo:
                x = np.linspace(xo, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 + r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 - r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, x0, y0 - r**0.5, x0, y0, r, 3)
                runin(x0, y0 - r**0.5, x0 + r**0.5, y0, x0, y0, r, 4)
                runin(x0 + r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 1)
                runin(x0, y0 + r**0.5, x0 - r**0.5, y0, x0, y0, r, 2)
                runin(x0 - r**0.5, y0, xe, ye, x0, y0, r, 3)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, xe, ye, x0, y0, r, 3)
                plt.show()
        # 起点在三象限,终点在第四象限
        elif xo <= x0 and yo <= y0 and xe >= x0 and ye <= y0 and xe > xo:
            x = np.linspace(xo, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0, y0 - r**0.5, x0, y0, r, 3)
            runin(x0, y0 - r**0.5, xe, ye, x0, y0, r, 4)
            plt.show()
        # 起点在三象限,终点在第一象限
        elif xo <= x0 and yo <= y0 and xe >= x0 and ye >= y0 and xe > x0:
            x = np.linspace(xo, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 + r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0, y0 - r**0.5, x0, y0, r, 3)
            runin(x0, y0 - r**0.5, x0 + r**0.5, y0, x0, y0, r, 4)
            runin(x0 + r**0.5, y0, xe, ye, x0, y0, r, 1)
            plt.show()
        # 起点在三象限,终点在第二象限
        elif xo <= x0 and yo <= y0 and xe <= x0 and ye >= y0 and ye > yo:
            x = np.linspace(xo, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 + r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0, y0 - r**0.5, x0, y0, r, 3)
            runin(x0, y0 - r**0.5, x0 + r**0.5, y0, x0, y0, r, 4)
            runin(x0 + r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 1)
            runin(x0, y0 + r**0.5, xe, ye, x0, y0, r, 2)
            plt.show()
        # 起点和终点在四象限
        elif xo >= x0 and yo <= y0 and xe >= x0 and ye <= y0:
            if ye == yo:
                x = np.linspace(xo, x0 + r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 - r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, x0 + r**0.5, y0, x0, y0, r, 4)
                runin(x0 + r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 1)
                runin(x0, y0 + r**0.5, x0 - r**0.5, y0, x0, y0, r, 2)
                runin(x0 - r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 3)
                runin(x0, y0 - r**0.5, xe, ye, x0, y0, r, 4)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin(xo, yo, xe, ye, x0, y0, r, 4)
                plt.show()
        # 起点在四象限,终点在第一象限
        elif xo >= x0 and yo <= y0 and xe >= x0 and ye >= y0 and ye > yo:
            x = np.linspace(xo, x0 + r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0 + r**0.5, y0, x0, y0, r, 4)
            runin(x0 + r**0.5, y0, xe, ye, x0, y0, r, 1)
            plt.show()
        # 起点在四象限,终点在第二象限
        elif xo >= x0 and yo <= y0 and xe <= x0 and ye >= y0 and xo > xe:
            x = np.linspace(xo, x0 + r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0 + r**0.5, y0, x0, y0, r, 4)
            runin(x0 + r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 1)
            runin(x0, y0 + r**0.5, xe, ye, x0, y0, r, 2)
            plt.show()
        # 起点在四象限,终点在第三象限
        elif xo >= x0 and yo <= y0 and xe <= x0 and ye <= y0 and xo > xe:
            x = np.linspace(xo, x0 + r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 - r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin(xo, yo, x0 + r**0.5, y0, x0, y0, r, 4)
            runin(x0 + r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 1)
            runin(x0, y0 + r**0.5, x0 - r**0.5, y0, x0, y0, r, 2)
            runin(x0 - r**0.5, y0, xe, ye, x0, y0, r, 3)
            plt.show()
    # 顺圆插补
    else:
        # 圆弧起点和终点均在第一象限
        if xo >= x0 and yo >= y0 and xe >= x0 and ye >= y0 and xo <= xe:
            if xo == xe:
                x = np.linspace(xo, x0 + r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 - r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, xe, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin1(xo, yo, x0 + r**0.5, y0, x0, y0, r, 1)
                runin1(x0 + r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 4)
                runin1(x0, y0 - r**0.5, x0 - r**0.5, y0, x0, y0, r, 3)
                runin1(x0 - r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 2)
                runin1(x0, y0 + r**0.5, xe, ye, x0, y0, r, 1)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)  # 这个表示在-5到5之间生成1000个x值
                # 对上述生成的1000个数循环用sigmoid公式求对应的y
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
                runin1(xo, yo, xe, ye, x0, y0, r, 1)
                plt.show()
        # 圆弧起点在第一象限, 终点在第四象限
        elif xo >= x0 and yo >= y0 and xe >= x0 and ye <= y0 and yo > ye:
            x = np.linspace(xo, x0 + r**0.5, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            x = np.linspace(x0 + r**0.5, xe, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
            runin1(xo, yo, x0 + r**0.5, y0, x0, y0, r, 1)
            runin1(x0 + r**0.5, y0, xe, ye, x0, y0, r, 4)
            plt.show()
        # 圆弧起点在第一象限, 终点在第三象限
        elif xo >= x0 and yo >= y0 and xe <= x0 and ye <= y0 and xo > xe:
            x = np.linspace(xo, x0 + r**0.5, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0 + r**0.5, y0, x0, y0, r, 1)
            runin1(x0 + r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 4)
            runin1(x0, y0 - r**0.5, xe, ye, x0, y0, r, 3)
            plt.show()
        # 圆弧起点在第一象限, 终点在第二象限
        elif xo >= x0 and yo >= y0 and xe <= x0 and ye >= y0 and xo > xe:
            x = np.linspace(xo, x0 + r**0.5, 1000)  # 这个表示在-5到5之间生成1000个x值
            # 对上述生成的1000个数循环用sigmoid公式求对应的y
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 - r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0 + r**0.5, y0, x0, y0, r, 1)
            runin1(x0 + r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 4)
            runin1(x0, y0 - r**0.5, x0 - r**0.5, y0, x0, y0, r, 3)
            runin1(x0 - r**0.5, y0, xe, ye, x0, y0, r, 2)
            plt.show()
        # 圆弧起点和终点均在第二象限
        elif xo <= x0 and yo >= y0 and xe <= x0 and ye >= y0 and xo <= xe:
            if xo == xe:
                x = np.linspace(xo, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 + r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 - r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, xe, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin1(xo, yo, x0, y0 + r**0.5, x0, y0, r, 2)
                runin1(x0, y0 + r**0.5, x0 + r**0.5, y0, x0, y0, r, 1)
                runin1(x0 + r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 4)
                runin1(x0, y0 - r**0.5, x0 - r**0.5, y0, x0, y0, r, 3)
                runin1(x0 - r**0.5, y0, xe, ye, x0, y0, r, 2)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)  # 这个表示在-5到5之间生成1000个x值
                # 对上述生成的1000个数循环用sigmoid公式求对应的y
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点
                runin1(xo, yo, xe, ye, x0, y0, r, 2)
                plt.show()
        # 圆弧起点第二象限,终点在第一象限
        elif xo <= x0 and yo >= y0 and xe >= x0 and ye >= y0 and xo < xe:
            x = np.linspace(xo, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0, y0 + r**0.5, x0, y0, r, 2)
            runin1(x0, y0 + r**0.5, xe, ye, x0, y0, r, 1)
            plt.show()
        # 圆弧起点第二象限,终点在第四象限
        elif xo <= x0 and yo >= y0 and xe >= x0 and ye <= y0 and xo < xe:
            x = np.linspace(xo, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 + r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0, y0 + r**0.5, x0, y0, r, 2)
            runin1(x0, y0 + r**0.5, x0 + r**0.5, y0, x0, y0, r, 1)
            runin1(x0 + r**0.5, y0, xe, ye, x0, y0, r, 4)
            plt.show()
        # 圆弧起点第二象限,终点在第三象限
        elif xo <= x0 and yo >= y0 and xe <= x0 and ye <= y0 and yo > ye:
            x = np.linspace(xo, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 + r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0, y0 + r**0.5, x0, y0, r, 2)
            runin1(x0, y0 + r**0.5, x0 + r**0.5, y0, x0, y0, r, 1)
            runin1(x0 + r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 4)
            runin1(x0, y0 - r**0.5, xe, ye, x0, y0, r, 3)
            plt.show()
        # 圆弧起点和终点均在第三象限
        elif xo <= x0 and yo <= y0 and xe <= x0 and ye <= y0 and xo >= xe:
            if xo == xe:
                x = np.linspace(xo, x0 - r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 + r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin1(xo, yo, x0 - r**0.5, y0, x0, y0, r, 3)
                runin1(x0 - r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 2)
                runin1(x0, y0 + r**0.5, x0 + r**0.5, y0, x0, y0, r, 1)
                runin1(x0 + r**0.5, y0, x0, y0 - r**0.5, x0, y0, r, 4)
                runin1(x0, y0 - r**0.5, xe, ye, x0, y0, r, 3)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin1(xo, yo, xe, ye, x0, y0, r, 3)
                plt.show()
        # 圆弧起点在第三象限，终点在第二象限
        elif xo <= x0 and yo <= y0 and xe <= x0 and ye >= y0 and ye > yo:
            x = np.linspace(xo, x0 - r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0 - r**0.5, y0, x0, y0, r, 3)
            runin1(x0 - r**0.5, y0, xe, ye, x0, y0, r, 2)
            plt.show()
        # 圆弧起点在第三象限，终点在第一象限
        elif xo <= x0 and yo <= y0 and xe >= x0 and ye >= y0 and xe > xo:
            x = np.linspace(xo, x0 - r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0 - r**0.5, y0, x0, y0, r, 3)
            runin1(x0 - r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 2)
            runin1(x0, y0 + r**0.5, xe, ye, x0, y0, r, 1)
            plt.show()
        # 圆弧起点在第三象限，终点在第四象限
        elif xo <= x0 and yo <= y0 and xe >= x0 and ye <= y0 and xe > xo:
            x = np.linspace(xo, x0 - r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 + r**0.5, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 + r**0.5, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0 - r**0.5, y0, x0, y0, r, 3)
            runin1(x0 - r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 2)
            runin1(x0, y0 + r**0.5, x0 + r**0.5, y0, x0, y0, r, 1)
            runin1(x0 + r**0.5, y0, xe, ye, x0, y0, r, 4)
            plt.show()
        # 圆弧起点和终点均在第四象限
        elif xo >= x0 and yo <= y0 and xe >= x0 and ye <= y0 and xo >= xe:
            if xo == xe:
                x = np.linspace(xo, x0, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 - r**0.5, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 - r**0.5, x0, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0, x0 + r**0.5, 1000)
                y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                x = np.linspace(x0 + r**0.5, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin1(xo, yo, x0, y0 - r**0.5, x0, y0, r, 4)
                runin1(x0, y0 - r**0.5, x0 - r**0.5, y0, x0, y0, r, 3)
                runin1(x0 - r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 2)
                runin1(x0, y0 + r**0.5, x0 + r**0.5, y0, x0, y0, r, 1)
                runin1(x0 + r**0.5, y0, xe, ye, x0, y0, r, 4)
                plt.show()
            else:
                x = np.linspace(xo, xe, 1000)
                y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
                plt.axis("equal")
                plt.plot(x, y)
                runin1(xo, yo, xe, ye, x0, y0, r, 4)
                plt.show()
        # 圆弧起点在第四象限,终点在第三象限
        elif xo >= x0 and yo <= y0 and xe <= x0 and ye <= y0 and xo > xe:
            x = np.linspace(xo, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0, y0 - r**0.5, x0, y0, r, 4)
            runin1(x0, y0 - r**0.5, xe, ye, x0, y0, r, 3)
            plt.show()
        # 圆弧起点在第四象限,终点在第二象限
        elif xo >= x0 and yo <= y0 and xe <= x0 and ye >= y0 and xo > xe:
            x = np.linspace(xo, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 - r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0, y0 - r**0.5, x0, y0, r, 4)
            runin1(x0, y0 - r**0.5, x0 - r**0.5, y0, x0, y0, r, 3)
            runin1(x0 - r**0.5, y0, xe, ye, x0, y0, r, 2)
            plt.show()
        # 圆弧起点在第四象限,终点在第一象限
        elif xo >= x0 and yo <= y0 and xe >= x0 and ye >= y0 and ye > yo:
            x = np.linspace(xo, x0, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, x0 - r**0.5, 1000)
            y = [-((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0 - r**0.5, x0, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            x = np.linspace(x0, xe, 1000)
            y = [((r - (i - x0)**2)**0.5) + y0 for i in x]
            plt.axis("equal")
            plt.plot(x, y)
            runin1(xo, yo, x0, y0 - r**0.5, x0, y0, r, 4)
            runin1(x0, y0 - r**0.5, x0 - r**0.5, y0, x0, y0, r, 3)
            runin1(x0 - r**0.5, y0, x0, y0 + r**0.5, x0, y0, r, 2)
            runin1(x0, y0 + r**0.5, xe, ye, x0, y0, r, 1)
            plt.show()


# 逆圆插补
def runin(xo, yo, xe, ye, x0, y0, r, k):
    p = float(e6.get())
    sum = int(abs(xo - xe) + abs(yo - ye))
    for i in range(int(sum/p)):
        if i == 0:
            txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")
        if k == 1:
            result3 = in_1(xo, yo, x0, y0, r)
        elif k == 2:
            result3 = in_2(xo, yo, x0, y0, r)
        elif k == 3:
            result3 = in_3(xo, yo, x0, y0, r)
        elif k == 4:
            result3 = in_4(xo, yo, x0, y0, r)
        # print(result3)
        plt.pause(0.5)
        plt.plot((xo, result3[0]), (yo, result3[1]))
        xo = result3[0]
        yo = result3[1]
        txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")


# 顺圆插补
def runin1(xo, yo, xe, ye, x0, y0, r, k):
    p = float(e6.get())
    sum = int(abs(xo - xe) + abs(yo - ye))
    for i in range(int(sum/p)):
        if i == 0:
            txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")
        # print(xo, yo)
        if k == 1:
            result3 = in_1_1(xo, yo, x0, y0, r)
        elif k == 2:
            result3 = in_1_2(xo, yo, x0, y0, r)
        elif k == 3:
            result3 = in_1_3(xo, yo, x0, y0, r)
        elif k == 4:
            result3 = in_1_4(xo, yo, x0, y0, r)
        # print(result3)
        plt.pause(0.5)
        plt.plot((xo, result3[0]), (yo, result3[1]))
        xo = result3[0]
        yo = result3[1]
        txt.insert(tkinter.INSERT, "(" + str(xo) + "," + str(yo) + ")" + "\n")


# 插补计算模块
# 在第一象限的插补
def in_1(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x - p
        y = y
    else:
        y = y + p
        x = x
    return (x, y)


def in_1_1(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x
        y = y - p
    else:
        y = y
        x = x + p
    return (x, y)


# 在第二象限的插补
def in_2(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x
        y = y - p
    else:
        y = y
        x = x - p
    return (x, y)


def in_1_2(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x + p
        y = y
    else:
        y = y + p
        x = x
    return (x, y)


# 在第三象限的插补
def in_3(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x + p
        y = y
    else:
        y = y - p
        x = x
    return (x, y)


def in_1_3(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x
        y = y + p
    else:
        y = y
        x = x - p
    return (x, y)


# 在第四象限的插补
def in_4(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x
        y = y + p
    else:
        y = y
        x = x + p
    return (x, y)


def in_1_4(x, y, x0, y0, r):
    p = float(e6.get())
    fm = (x - x0)**2 + (y - y0)**2 - r
    if fm >= 0:
        x = x - p
        y = y
    else:
        y = y - p
        x = x
    return (x, y)


# 清除数据
def clear():
    txt.delete(0.0, tkinter.END)


# tkinter创建窗口
win = tkinter.Tk()
win.title("hwy")
win.geometry("600x400")
win.resizable(width=False, height=False)
label = tkinter.Label(win, text="圆弧插补")
label.pack()
button = tkinter.Button(win, text="插补计算", command=show)
button.place(x=250, y=350)
R1 = tkinter.IntVar()
radio3 = tkinter.Radiobutton(win, text="顺圆插补", value=11, variable=R1)
radio3.place(x=100, y=300)
radio4 = tkinter.Radiobutton(win, text="逆圆插补", value=22, variable=R1)
radio4.place(x=200, y=300)
R1.set(11)

label2 = tkinter.Label(win, text="起点坐标：Xo=")
label2.place(x=100, y=50)
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
e.set(0)
entry.place(x=200, y=50)
label3 = tkinter.Label(win, text="起点坐标：Yo=")
label3.place(x=100, y=80)
e1 = tkinter.Variable()
entry1 = tkinter.Entry(win, textvariable=e1)
e1.set(10)
entry1.place(x=200, y=80)

label4 = tkinter.Label(win, text="终点坐标：Xe=")
label4.place(x=100, y=110)
e2 = tkinter.Variable()
entry2 = tkinter.Entry(win, textvariable=e2)
e2.set(10)
entry2.place(x=200, y=110)

label5 = tkinter.Label(win, text="终点坐标：Ye=")
label5.place(x=100, y=140)
e3 = tkinter.Variable()
entry3 = tkinter.Entry(win, textvariable=e3)
e3.set(0)
entry3.place(x=200, y=140)

label6 = tkinter.Label(win, text="圆心坐标：X=")
label6.place(x=100, y=170)
e4 = tkinter.Variable()
entry4 = tkinter.Entry(win, textvariable=e4)
e4.set(0)
entry4.place(x=200, y=170)

label7 = tkinter.Label(win, text="圆心坐标：Y=")
label7.place(x=100, y=200)
e5 = tkinter.Variable()
entry5 = tkinter.Entry(win, textvariable=e5)
e5.set(0)
entry5.place(x=200, y=200)

label8 = tkinter.Label(win, text="脉冲当量：P=")
label8.place(x=100, y=230)
e6 = tkinter.Variable()
entry6 = tkinter.Entry(win, textvariable=e6)
e6.set(1)
entry6.place(x=200, y=230)

label9 = tkinter.Label(win, text="精度：A=")
label9.place(x=100, y=260)
e7 = tkinter.Variable()
entry7 = tkinter.Entry(win, textvariable=e7)
e7.set(5)
entry7.place(x=200, y=260)
# 显示坐标值
txt = tkinter.Text(win)
txt.place(x=400, y=30)
button1 = tkinter.Button(win, text="清除坐标", command=clear)
button1.place(x=340, y=350)
win.mainloop()
