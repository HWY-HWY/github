"""
os模块包含了操作系统的一些普通功能，也可以处理文件
"""

import os
# 获取操作系统类型， nt--Windows， posix--UNIX、Linux
print(os.name)
# 获取操作系统的详细信息，Windows不支持，Linux支持
# print(os.uname())
# 获取所有的环境变量
# print(os.environ)
# # 获取指定的环境变量
# print(os.environ.get("ADAMS_GUI_LOCALE"))
# 获取当前目录 相对路径
# print(os.curdir)
# # 获取绝对路径
# print(os.getcwd())
# 返回指定路径下的所有文件（第一级）
# print(os.listdir(r"D:\python源文件"))
# 创建和删除目录
# os.mkdir("hwy")
# os.rmdir('hwy')


# 获取文件属性
# print(os.stat("django"))

# 重命名文件
# os.rename('hwy', 'myy')

# 删除普通文件
# os.remove("1.txt")

# 运行shell命令
# 打开记事本
# os.system("notepad")
# 打开写字板
# os.system("write")
# 打开画图板
# os.system("mspaint")
# 打开设置
# os.system("msconfig")
# 设置关机 最后一位数值代表延时时间，单位s
# os.system("shutdown -s -t 500")
# 取消关机
# os.system("shutdown -a")
# 关闭进程
# os.system("taskkill /f /im 进程名")

# 查看指定位置的绝对路径
# print(os.path.abspath("."))

# 拼接路径,第二个参数不能以\开头
# path1 = os.path.abspath(".")
# path2 = r"hwy\a"
# print(os.path.join(path1, path2))

# 拆分路径
path1 = r"D:\python源文件\hwy\a.txt"
path2 = "hwy\a"
# # 拆分最底层
# print(os.path.split(path1))
# # 拆分最底层扩展名
# print(os.path.splitext(path1))
# 获取文件名
# print(os.path.basename(path1))

# 判断是否为目录
# print(os.path.isdir(path2))

# 判断文件是否存在
# print(os.path.isfile(path1))

# 判断目录是否存在
# print(os.path.exists(path1))

# 创建了一个目录和一个文件
# os.mkdir("hwy")
# f = open("./hwy/a.txt", "w")
# f.close()

# 获取文件的大小 单位字节
# print(os.path.getsize(path1))
