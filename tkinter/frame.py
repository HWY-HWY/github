'''
frame控件，作为框架容器使用
'''

import tkinter

win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# 在win下创建一个frame容器
frame = tkinter.Frame(win)
frame.pack()
# 在frame容器的左边创建一个frame1容器
frame_1 = tkinter.Frame(frame)
# 再在frame_1这个容器中创建标签
tkinter.Label(frame_1, text="左上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frame_1, text="左下", bg="pink").pack(side=tkinter.TOP)
frame_1.pack(side=tkinter.LEFT)
# 在frame容器的左边创建一个frame容器
frame_2 = tkinter.Frame(frame)
# 再在frame_2这个容器中创建标签
tkinter.Label(frame_2, text="右上", bg="yellow").pack(side=tkinter.TOP)
tkinter.Label(frame_2, text="右下", bg="blue").pack(side=tkinter.TOP)
frame_2.pack(side=tkinter.RIGHT)

win.mainloop()
