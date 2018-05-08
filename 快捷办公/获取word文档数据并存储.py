"""
存储word文档
"""

import win32com
import win32com.client


def writewordtopath(path, topath):
    # 调用win32的word功能，支持docx和doc两种格式的文件
    mw = win32com.client.Dispatch("Word.APPlication")
    # 打开文件
    doc = mw.Documents.Open(path)
    # 将数据存储到txt中 2表示存到txt中
    doc.SaveAs(topath, 2)
    # 关闭文件
    doc.Close()
    # 关闭word功能
    mw.Quit()


path = r"C:\Users\Administrator\Desktop\word.docx"
topath = r"C:\Users\Administrator\Desktop\a.txt"
writewordtopath(path, topath)
