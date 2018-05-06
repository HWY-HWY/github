"""
文本控件，用于显示多行文本
"""


import tkinter


win = tkinter.Tk()
win.title("hwy")
win.geometry('400x400+400+200')
# 创建滚动条
s = tkinter.Scrollbar()
s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text = tkinter.Text(win, width=40, height=2)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
# 关联
s.config(command=text.yview)
text.config(yscrollcommand=s.set)
str = "life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf \
is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg\
life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg\
life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg\
life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg \
is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg\
life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg\
life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg\
life is shsdasdasdasdasdaasfw  fsdfs sdfsdg gfdgdf fgdfg"
text.insert(tkinter.INSERT, str)
win.mainloop()
