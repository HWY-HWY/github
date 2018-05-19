import urllib.request
import json

url = r'http://127.0.0.1:8000/index/'
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)
print(type(data))
# 将json格式的数据转化为Python数据类型
jsondata = json.loads(data)
print(jsondata["name"])
print(type(jsondata))
