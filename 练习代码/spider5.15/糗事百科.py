
import urllib.request
import re


def spider(url):
    # 创建请求头，用来模拟浏览器请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
    }
    # 创建请求体
    req = urllib.request.Request(url, headers=headers)
    # 请求
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    return data


url = r"https://www.qiushibaike.com/text/page/2/"
re_txt1 = ''
re_txt2 = ''
re_txt = r'<div class="content">\n<span>([\S\s]*?)</span>'
print(type(re_txt))
result = spider(url)
# txt = re.compile(re_txt)
# with open(r"C:\Users\Administrator\Desktop\qiu.txt", "w", encoding="utf-8") as f:
#     f.write(result)
# print(result)
result = re.findall(re_txt, result)
print(result)
