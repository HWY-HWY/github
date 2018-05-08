"""
创建word文档
"""

import win32com
import win32com.client
import os


def makeword(path, name):
    # 调用win32的word功能，支持docx和doc两种格式的文件
    mw = win32com.client.Dispatch("Word.APPlication")
    # 让文档可见
    mw.visible = True

    # 创建文档
    doc = mw.Documents.Add()

    # 写内容
    # 从头开始写
    r = doc.Range(0, 0)
    r.InsertAfter("你好" + name + "\n")
    r.InsertAfter("-------------很高兴认识你！")
    # 存储文件
    doc.SaveAs(path)
    # 关闭文件
    doc.Close()
    # 关闭word功能
    mw.Quit()


names = ['python', 'java', 'c++']
path = "C:\\Users\\Administrator\\Desktop\\"
for name in names:
    newpath = os.path.join(path, name)
    makeword(newpath, name)
