"""
鼠标右键菜单
"""


import tkinter


win = tkinter.Tk()
win.title("hwy")
win.geometry("400x400")
# 创建菜单条
menubar = tkinter.Menu(win)
# 创建菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
# 给菜单选项添加内容
for item in ['python', "c++", "C", "PHP", "java", "C#", "quit"]:
    if item == "quit":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item)
# 向菜单条上添加菜单选项
menubar.add_cascade(label="语言", menu=menu1)

# 以上只是创建了菜单，但是并没有显示，下面就通过鼠标右键这个事件来显示菜单


def showmenu(event):
    menubar.post(event.x_root, event.y_root)


win.bind('<Button-3>', showmenu)
win.mainloop()
