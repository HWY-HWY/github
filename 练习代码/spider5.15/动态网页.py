import urllib.request
import json
import ssl


def spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
    }
    # 创建请求体
    req = urllib.request.Request(url, headers=headers)
    # 使用ssl创建不验证的上下文，从而可以爬取https安全网站
    context = ssl._create_unverified_context()
    # 发起请求
    reponse = urllib.request.urlopen(req, context=context)
    data = reponse.read().decode("utf-8")
    data = json.loads(data)
    return data


# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1"
# result = spider(url)
# print(result)
# print(len(result))
j = 1
for i in range(0, 10):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i * 20) + "&limit=20"
    result = spider(url)
    for info in result:
        with open(r"C:\Users\Administrator\Desktop\dou.txt", "a", encoding="utf-8") as f:
            f.write(str(j) + info["title"] + "\n")
            j = j + 1
    print(len(result))
