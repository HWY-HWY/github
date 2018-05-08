

path = r"C:\Users\Administrator\Desktop\1234.txt"

with open(path, "wb") as f:
    str = "hwy is a good man黄"
    f.write(str.encode("utf-8"))

with open(path, "rb", errors="ignore") as f1:
    data = f1.read()
    # 得到的是一个二进制文件
    print(data)
    print(type(data))
    # 解码,需要注意的是：解码和编码格式需要一致
    newdata = data.decode("gbk")
    print(newdata)
    print(type(newdata))
