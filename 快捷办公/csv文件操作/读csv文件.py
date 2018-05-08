"""
读取csv文件中的数据
"""

import csv


def readcsv(path):
    # 以只读模式打开path路径所指的文件
    with open(path, "r") as f:
        # 用csv中的reader方法打开文件，获得的是一个对象
        alldata = csv.reader(f)
        datalist = []
        for row in alldata:
            datalist.append(row)
        return datalist


path = r"D:\Python数据\csv数据.csv"
result = readcsv(path)
print(result)
