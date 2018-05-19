import json

# 将Python数据转化为json数据类型
data = {"name": "hwy", "age": "20"}
jsondata = json.dumps(data)
print(jsondata)
print(type(jsondata))
# 将data这个字典以json数据类型写入本地
path = r"C:\Users\Administrator\Desktop\hwy.json"
# with open(path, "w") as f:
#     json.dump(data, f)
# 读取本地的json数据
with open(path, "r") as f:
    r = f.read()
    print(r)
    print("--------")
    print(type(r))
    newr = json.loads(r)
    print(newr)
    print(type(newr))
