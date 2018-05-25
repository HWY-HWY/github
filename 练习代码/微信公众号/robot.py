import requests
import json
# import time


def robot(content):
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # userid = int(time.time())
    data = {
        "perception": {
            "inputText": {
                "text": content
                         }
                      },
        "userInfo": {
                    "apiKey": "672035b1bde5440e83eaexxxxxxxx",
                    "userId": '672035b1bde5440',
                    }
    }
    jsondata = json.dumps(data)
    response = requests.post(api, data=jsondata)
    robot_res = json.loads(response.content)
    print(robot_res["results"][0]['values']['text'])


while True:
    content = input("talk:")
    robot(content)
