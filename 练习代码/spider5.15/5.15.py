import urllib.request

# 通过urlopen这个方法向指定的url发送请求，并放回服务器响应的数据
response = urllib.request.urlopen("https://www.douban.com/")
# 通过read读取返回的全部数据，并通过decode指定编码方式,赋值给一个字符变量
# data = response.read().decode("utf-8")
# 每次读取一行内容，可以通过循环来读取数据
data1 = response.readline().decode("utf-8")
# 读取全部数据，但是赋值给一个列表变量，每一行为一个元素
data2 = response.readlines()
print(data2[100].decode("utf-8"))
# 放回当前环境的相关信息
print(response.info())
# 返回状态码 200 成功访问， 304 存在缓存
print(response.getcode())
# 返回当前请求的网址
print(response.geturl())
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=\
monline_3_dg&wd=%E7%99%BE%E5%BA%A6&oq=charles%25E4%25B8%258B%2\
5E8%25BD%25BD&rsv_pq=e61190b5000004db&rsv_t=a6c11nbP3rDI9y0Mz%\
2FODHo%2FT6%2F9jLULDmr6tH5cVepSLYjyv0V0ewhGEzBUwlZoNRhfw&rqlan\
g=cn&rsv_enter=1&rsv_sug3=6&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0\
&inputT=896&rsv_sug4=13910"
# 转义网址中的中文编码
newurl = urllib.request.unquote(url)
# print(newurl)
url1 = "黄文杨"
# 与unquote过程相反
newurl = urllib.request.quote(url1)
print(newurl)
