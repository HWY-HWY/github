import urllib.request
import re
import os


def spider(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"
    }
    # 创建请求体
    req = urllib.request.Request(url, headers=headers)
    # 发起请求
    response = urllib.request.urlopen(req)
    html_data = response.read().decode("utf-8")
    return html_data


url = "http://588ku.com/sucai/0-pxnum-0-0-0-1/?h=360&sem=1"
result = spider(url)
re_str = r'data-original="([\s\S]*?)!/fw/254/quality/90/unsharp/true/compress/true"'
img_url_str = re.findall(re_str, result)
img_path = r"C:\Users\Administrator\Desktop\img"
num = 1
for img_url in img_url_str:
    # 拼接路径
    img_name = os.path.join(img_path, str(num) + ".jpg")
    num += 1
    # 通过url下载对应的图片并保存到本地
    urllib.request.urlretrieve(img_url, filename=img_name)
