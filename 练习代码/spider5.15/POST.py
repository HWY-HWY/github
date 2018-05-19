import urllib.request
import urllib.parse

url = "http://127.0.0.1:8000/form/"
# 创建请求所需的数据
re_data = {
    "username": "hwy",
    "passwd": "123",
}
# 将数据进行打包,并指定编码格式
post_data = urllib.parse.urlencode(re_data).encode("utf-8")
# 构造请求体
req = urllib.request.Request(url, post_data)
# 请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
