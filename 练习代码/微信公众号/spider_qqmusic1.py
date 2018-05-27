# -*-coding:utf-8-*-
# encoding =utf-8
import requests
import json
from time import time


# 利用时间戳创建guid参数
guid = str(int(time()))
# 创建请求头，必须要保证整个过程的guid的值要相同
hea = {
        "User_Agent": r"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "cookie": 'pgv_pvi=9563846656; pgv_si=s4264375296; pgv_pvid=%s; qqmusic_fromtag=66' % guid,
        "Referer": "https://y.qq.com/n/yqq/song/003vUjJp3QwFcd.html",
        "Host": "c.y.qq.com"
    }


# 得到歌曲id
def spider1(url):
    # 发起请求
    response = requests.get(url, headers=hea)
    # 转化为json数据，提取得到歌曲id
    data_list = json.loads(response.text[34:-1])['data']['song']['list'] 
    music_id = data_list[0]["id"]
    mid = data_list[0]["mid"]
    # 返回id和mid，后面发起请求是要用到这两个参数
    return (music_id, mid)


# 得到歌曲的歌词信息
def spider2(music_id):
    url = r"https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg?nobase64=1"
    url += "&musicid=" + str(music_id) + r"&callback=jsonp1&g_tk=5381&jsonpCall\
    back=jsonp1&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-\
    8&notice=0&platform=yqq&needNewCode=0"
    response = requests.get(url, headers=hea)
    print(response.text)


# 得到vkey
def spider3(mid):
    url = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?\
    g_tk=5381&jsonpCallback=MusicJsonCallback93443074145225121&loginUin=0&h\
    ostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=y\
    qq&needNewCode=0&cid=205361747&callback=MusicJsonCallback9344307414522512&\
    uin=0&songmid=%s&filename=C400%s.m4a&guid=%s" % (mid, mid, guid)
    response = requests.get(url)
    data = response.text[34:-1]
    vkey = json.loads(data)["data"]["items"][0]["vkey"]
    filename = json.loads(data)["data"]["items"][0]["filename"]
    return (vkey, filename)


music_keword = input("keyword:")
print(music_keword)
print(type(music_keword))
url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&\
qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=57\
319834734357796&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p\
=1&n=20&w=%s&g_tk=5381&jsonpCallback=MusicJsonCallback799849464782\
1491&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=ut\
f-8&notice=0&platform=yqq&needNewCode=0" % (music_keword)
id_list = spider1(url)
spider2(id_list[0])
data = spider3(id_list[1])
# 拼接数据得到音乐的播放url
music_url = "http://dl.stream.qqmusic.qq.com/%s?vkey=%s&guid=%s&uin=0&fromtag=66" % (data[1], data[0], guid)
print(music_url)
