import requests
import base64
import json
import time


def face(imgurl):
    # 通过imgurl对图片进行base64编码
    img_content = requests.get(imgurl).content
    img_base = base64.b64encode(img_content)
    # 将进过编码的图片post给微软服务器
    ms_url1 = r"https://kan.msxiaobing.com/Api/Image/UploadBase64"
    # 获得图片在微软服务器的url
    img_ms_response = requests.post(ms_url1, data=img_base)
    # 转化为json格式，便于取数据
    img_ms_response_json = json.loads(img_ms_response.content)
    # 得到微软url
    img_ms_url = img_ms_response_json["Host"] + img_ms_response_json["Url"]
    # 请求测评
    ms_url2 = r"https://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi&tid=1f2dc8a381324b5f94b5eb8a2b212587"
    # 构造post请求头，其中cookie和referer不可缺，否则返回null
    hea = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Cookie": "cpid=YDAgSSFJxkheSixMfkkoMc-wlEznNFpIJzU-MyMzLUlIAA; salt=A3C081625F837C904F3BE4D202A74964; ai_user=WIdda|2018-05-22T02:25:08.861Z; ARRAffinity=b3bb36113778459332a680fea7d54df0c62e27d3ae6c8c7b478813f608a7df2e; ai_session=8l4ET|1527230783058|1527232952732",
        "Referer": "https://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi&feid=d9bbc18bf094ae43de8ce0bbc3943d42",
    }
    # 构造post数据
    data = {
        "Content[imageUrl]": img_ms_url,
        "CreateTime": int(time.time()),
    }
    # 发起请求
    response = requests.post(ms_url2, data=data, headers=hea)
    # 转化为json数据
    content_json = json.loads(response.content)
    content = content_json["content"]["text"]
    print(content)


img_url = r"http://mmbiz.qpic.cn/mmbiz_jpg/rViaJzEiap09VAhbw9c8WAzcfibic5icTnjerddrBvpoibDp0XficPw6QZcDIFffcmVFKjk7UOj6aFM1Rxks1XzHBAcMg/0"
face(img_url)
