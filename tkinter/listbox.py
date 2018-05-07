'''
listbox 控件
'''


import tkinter


win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# 绑定参数
lbv = tkinter.StringVar()
listbox = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE, listvariable=lbv,)
str = ["python", "java", "php", "C++", "C#"]
# 增加参数
for text in str:
    listbox.insert(tkinter.END, text)
listbox.insert(tkinter.ACTIVE, "HTML")
# 删除参数, 有两个参数，第一个参数指定开始的索引，第二个参数指定
# 结束的索引，如果只有一个参数则只删除一个
# listbox.delete(1)
# # 选中，参数同delete
listbox.select_set(1, 3)
# # 清除选中，参数同delete
# listbox.select_clear(2)
# # 获取元素的个数
# print(listbox.size())
# # 获得指定下标的值
# print(listbox.get(1, 3))
# 返回当前选中项的标号
# print(listbox.curselection())
# 判断一个元素是否被选中
# print(listbox.select_includes(1))
# 修改元素的内容
# lbv.set(('1', '2', '3'))
# 绑定事件


# def showinfo(event):
#     print(listbox.get(listbox.curselection()))


# listbox.bind('<Double-Button-1>', showinfo)
# print(lbv.get())
listbox.pack()
win.mainloop()
