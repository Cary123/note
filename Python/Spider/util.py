import os
import datetime
import json
import requests
import time
import random
import hashlib
import sys
import uuid
from urllib import request,parse

cookie1 = "OUTFOX_SEARCH_USER_ID=42474381@10.168.1.241; JSESSIONID=aaawRmNTElH3Q4_wUlzKw; OUTFOX_SEARCH_USER_ID_NCOO=1959109122.590772; ___rl__test__cookies="
UserAgent1 = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36"

cookie2 = "OUTFOX_SEARCH_USER_ID=1281446577@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1657408785.351486; JSESSIONID=aaagQ645r8G2mgAkry-Kw; SESSION_FROM_COOKIE=unknown; UM_distinctid=1694318b46b1b8-01e2ca30c4c557-b781636-100200-1694318b46c238; ___rl__test__cookies="
UserAgent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_KEY = '6f912dba431c0b6d'
APP_SECRET = 'O1C6GatJgXxStWT7QN54ESmyQSrp6H90'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def youdaoAPI(q, retry):
    try:
        if (retry > 5):
            return ""
        data = {}
        data['from'] = 'EN'
        data['to'] = 'zh-CHS'
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
        sign = encrypt(signStr)
        data['appKey'] = APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign

        response = do_request(data)
        result = json.loads(response.content)
        itms = result['translation']
        content = ""
        for item in itms:
            content += item
        return content
    except Exception as e:
        return youdaoAPI(q, retry + 1)

def getMD5(value):
    aa = hashlib.md5()
    aa.update(bytes(value,encoding="utf-8"))
    sign = aa.hexdigest()
    return sign

def translate(word):
    #return youdaoAPI(word, 0)
    return youDaoTranslate(word, 0)

# youdao translate
def youDaoTranslate(word, retry):
    try:
        if (retry > 3):
            return ""
        cookie = cookie1
        userAgent = UserAgent1
        if (retry % 2 != 0):
            cookie = cookie2
            userAgent = UserAgent2
        salt = int(time.time() *10000)
        ts = int(time.time() * 1000)
        value = "fanyideskweb" + word + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        data= {
            "i":word,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":salt,
            "sign":getMD5(value),
            "ts":ts,
            "bv":"5933be86204903bb334bf023bf3eb5ed",
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTIME",
            "typoResult":"false"
        }
        data_str = parse.urlencode(data)
        headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                "Accept - Encoding":"gzip, deflate, br",
                'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
                'Connection': 'keep-alive',
                'Cache-Control': 'no-cache',
                'Content-Length': str(len(data_str)),
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': cookie + str(time.time() * 1000),
                'Host': 'fanyi.youdao.com',
                'Origin': 'http://fanyi.youdao.com',
                'Referer': 'http://fanyi.youdao.com/',
                'Pragma': 'no-cache',
                'User-Agent': userAgent,
                'X-Requested-With': 'XMLHttpRequest'
            }

        # req = request.Request(url=url,data=bytes(data_str,encoding='utf-8'),headers=headers)
        # content = request.urlopen(req).read().decode('utf-8')
        s = requests.session()
        content = s.post(url,data= data,headers = headers).text
        result = json.loads(content)
        translateContent = ''
        for item1 in result['translateResult']:
            for item2 in item1:
                translateContent += item2['tgt']
        return translateContent 
    except Exception as e:
        return youDaoTranslate(word, retry + 1)

#Enter log
def log(txt):
    fo = open(r"F:\mayun\Note\Python\Spider\log\log.txt", "a+")
    fo.write(str(datetime.datetime.today())+"\n")
    fo.write(txt+"\n")
    fo.write("\n")
    fo.close()

if __name__ == "__main__":
    print(translate("When in the group, he will stand slightly away so as to appear alone. Do you see him adjusting his tie, or making exaggerated movements or gestures? This means he is trying to stand out of the crowd. He wants to attract your attention towards him. He wants you to notice him like he has been noticing you."))

