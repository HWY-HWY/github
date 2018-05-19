import urllib.request
import re
import os


def spider(url):
    # 创建请求头，模拟浏览器请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
    }
    # 利用请求头来创建请求体
    req = urllib.request.Request(url, headers=headers)
    # 发起请求
    response = urllib.request.urlopen(req)
    # 获得放回的数据并指定解码格式
    data = response.read().decode('UTF-8')
    return data


url = r"http://www.tgirl.cc/gctt/kimoe"
result = spider(url)
# 正则字符串
re_str1 = r'<span class="read-more"><a href="([\s\S]*?)">阅读全文»</a></span>'
re_str2 = r'<div id="post_content">([\s\S]*?)<div class="xydown_down_link">'
re_str3 = r'<img src="([\s\S]*?)" alt="'
img_url_list1 = re.findall(re_str1, result)
num = 1
# 图片存储的路径
path = r"C:\Users\Administrator\Desktop\img"
# 打开对应的总览的链接
for img_url_l in img_url_list1:
    # 打开总览后返回的数据
    download_html = spider(img_url_l)
    download_url = re.findall(re_str2, download_html)
    img_url_list2 = re.findall(re_str3, download_url[0])
# print(download_url)
# 下载图片到本地
    for img in img_url_list2:
        filename = os.path.join(path, str(num) + ".jpg")
        urllib.request.urlretrieve(img, filename=filename)
        print(img)
        num += 1
