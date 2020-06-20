# coding = utf-8
import urllib,re,requests
import sys
import json
import os
from bs4 import BeautifulSoup

headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
 'Cookie':'MUID=0DA4D4BD498D6CFB3AA9D9BE4D8D6820; _SS=SID=00; videoCookiesLastCategory=en-ca=animals; _cb_ls=1; _cb=DsAPZCJmzJ0BiCB2c; _chartbeat2=.1550504320201.1550509083431.11.uAsG96ZMUeDgWcawC2JWWNCmna0Z.1; ANON=A=E43533FD3C93526D33F4F5C4FFFFFFFF&E=164d&W=1; NAP=V=1.9&E=15f3&C=gBm5NGQ6hq9_2JLke_9M_uUX-nhzUVJp3UwliRTchLXC4pE05Iv2DA&W=1; vidvol=10; adoptout={"msaOptOut":0,"adIdOptOut":0}; videoerrorcount=0; trg=0%7C0%7C0; ecasession=v2_9a22cfec7b49fc3893239e7b074a63fd_ba74fcd1-eff2-48d8-b6af-082423d58358-tuct35eea8e_1550666026_1550666984_CNawjgYQqLw-GP6e37rd9J7zBiACKAYwMDjK_QdA_qAQSI7OHlCJxAlYAGAC'
}

keyWords = ["古装","汉风","古风", "汉服", "cosplay"]

def download(url, path):
    if (not os.path.exists(path)):
        urllib.request.urlretrieve(url, path)

def validateUrl(soup):
    found = False
    lists = soup.select('.head-line h1')
    if len(lists) > 0:
        article = lists[0].text
        for keyword in keyWords:
            if keyword in article:
                found = True
                break
    return found

def analysisImg(soup):
    lists = soup.select('.baidu_image_holder img')
    if len(lists) > 0:
        imgUrl = lists[0]["src"]
        name = imgUrl[imgUrl.rfind("/")+1:]
        targetFile = os.path.join(targetDir, name+'.jpg')
        download(imgUrl, )
    return found
    

def analysisAndDownload(url):
    targetDir= r"H:\自媒体\图片\huaban"
    res = requests.get(url, headers = headers)
    if res.status_code == 200:
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, 'html.parser')
        if validateUrl(soup):
            title = soup.select('.head-line h1')[0].text
            dir = targetDir + r"\" + title
            if not os.path.exists():
                os.makedirs(dir)

if __name__ == "__main__":
    # targetDir= r"H:\自媒体\图片\huaban"
    # url = "https://huaban.com/pins/"
    # start = 2243143640
    # end = 3243143640
    # for i in range(start, end):
    #     url = url + str(i)
    # targetFile = os.path.join(targetDir, '111.jpg')
    # download('https://hbimg.huabanimg.com/d818b5c6890a9139bbd70d5c21101dc6beb0ce4894495-Tpz6pL_fw658', targetFile)
    analysisAndDownload()
