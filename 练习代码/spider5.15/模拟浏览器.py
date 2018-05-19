import urllib.request


url = r"http://www.huangwenyang.cn/"
# 构造一个请求头，里面包含一些关于浏览器的信息，比如版本、内核等
header = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"
}
# 构造一个请求体，里面包含请求头，这样就模拟浏览器访问了
req = urllib.request.Request(url, headers=header)
# 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
