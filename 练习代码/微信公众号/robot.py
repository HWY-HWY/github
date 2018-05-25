import requests
import json
# import time


# 创建post函数
def robot(content):
    # 图灵api
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # userid = int(time.time())
    # 创建post提交的数据
    data = {
        "perception": {
            "inputText": {
                "text": content
                         }
                      },
        "userInfo": {
                    "apiKey": "672035b1bde5440e83eaexxxxxxx",
                    "userId": '672035b1bde5440',
                    }
    }
    # 转化为json格式
    jsondata = json.dumps(data)
    # 发起post请求
    response = requests.post(api, data=jsondata)
    # 将返回的json数据解码
    robot_res = json.loads(response.content)
    # 提取对话数据
    print(robot_res["results"][0]['values']['text'])


# 创建对话死循环
while True:
    # 输入对话内容
    content = input("talk:")
    robot(content)
