"""
实现树状的结构，类似文件夹的结构
"""


import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
tree = ttk.Treeview(win)
tree.pack()
# 创建一级菜单
tree1 = tree.insert("", 0, "成都", text="成都")
tree2 = tree.insert("", 1, "自贡", text="自贡")
tree3 = tree.insert("", 2, "上海", text="上海")
# 创建二级菜单
tree1_1 = tree.insert(tree1, 0, "郫县", text="郫县")
tree1_2 = tree.insert(tree1, 1, "武侯", text="武侯")
tree1_3 = tree.insert(tree1, 2, "金牛", text="金牛")


tree2_1 = tree.insert(tree2, 0, "富顺", text="富顺")
tree2_2 = tree.insert(tree2, 1, "12", text="12")
tree2_3 = tree.insert(tree2, 2, "23", text="23")
win.mainloop()
