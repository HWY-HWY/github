"""
写csv文件
"""


import csv


def writecsv(path, data):
    # 以写的方式打开一个文件，如果没有则创建
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowdata in data:
            writer.writerow(rowdata)


path = r"D:\Python数据\csv数据写入.csv"
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
writecsv(path, data)
