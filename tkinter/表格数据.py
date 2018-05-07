"""
显示表格数据
"""

import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("hwy")
win.geometry("600x400")
# 创建表格
tree = ttk.Treeview(win)
tree.pack()
# 创建列
tree["columns"] = ("姓名", "年龄", "身高", "体重")
# 设置列，只是设置了属性，但是还是不能显示
tree.column("姓名", width=100)
tree.column("年龄", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)
# 设置表头，这里才设置显示的内容
tree.heading('姓名', text='-姓名-')
tree.heading('年龄', text='-年龄-')
tree.heading('身高', text='-身高-')
tree.heading('体重', text='-体重-')
# 添加数据
tree.insert('', 0, text='1', value=('python', '18', '20', '30'))
tree.insert('', 1, text='2', value=('java', '18', '20', '30'))
win.mainloop()
