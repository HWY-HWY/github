import urllib.request

url = r"http://www.huangwenyang.cn/"

for i in range(50):
    try:
        req = urllib.request.urlopen(url, timeout=0.01)
        print("----------------")
    except:
        print("请求超时！")
