"""
读取word文档
"""

import win32com
import win32com.client


def writeword(path):
    # 调用win32的word功能，支持docx和doc两种格式的文件
    mw = win32com.client.Dispatch("Word.APPlication")
    # 打开文件
    doc = mw.Documents.Open(path)
    # 以行为单位取数据，取出的格式为str
    for data in doc.Paragraphs:
        line = data.Range.Text
        print(line)

    # 关闭文件
    doc.Close()
    # 关闭word功能
    mw.Quit()


path = r"C:\Users\Administrator\Desktop\word.docx"
writeword(path)
