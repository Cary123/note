# coding = utf-8
import urllib,re,requests
import sys
import util
import json
import os
from bs4 import BeautifulSoup

headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
 'Cookie':'MUID=0DA4D4BD498D6CFB3AA9D9BE4D8D6820; _SS=SID=00; videoCookiesLastCategory=en-ca=animals; _cb_ls=1; _cb=DsAPZCJmzJ0BiCB2c; _chartbeat2=.1550504320201.1550509083431.11.uAsG96ZMUeDgWcawC2JWWNCmna0Z.1; ANON=A=E43533FD3C93526D33F4F5C4FFFFFFFF&E=164d&W=1; NAP=V=1.9&E=15f3&C=gBm5NGQ6hq9_2JLke_9M_uUX-nhzUVJp3UwliRTchLXC4pE05Iv2DA&W=1; vidvol=10; adoptout={"msaOptOut":0,"adIdOptOut":0}; videoerrorcount=0; trg=0%7C0%7C0; ecasession=v2_9a22cfec7b49fc3893239e7b074a63fd_ba74fcd1-eff2-48d8-b6af-082423d58358-tuct35eea8e_1550666026_1550666984_CNawjgYQqLw-GP6e37rd9J7zBiACKAYwMDjK_QdA_qAQSI7OHlCJxAlYAGAC'
}

keyWords = ["嫩", "胸","乳","奶", "裸", "骚", "淫", "美女", "妖精", "长腿", "清纯"]

def fetchUrl(url):
    res = requests.get(url, headers = headers)
    found = False
    if res.status_code == 200:
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, 'html.parser')
        lists = soup.select('.ArticleTitle strong')
        if len(lists) > 0:
            article = lists[0].text
            for keyword in keyWords:
                if keyword in article:
                    found = True
                    break
    return found

def analysisAndWriteUrl(url):
    try:
        res = requests.get(url, headers = headers)
        if res.status_code == 200:
            res.encoding = 'utf8'
            soup = BeautifulSoup(res.text, 'html.parser')
            lists = soup.select('.ImageBody img')
            if len(lists) > 0:
                imgUrl = lists[0]["src"]
                WriteImgUrlToFile(imgUrl)
            if "_" in url:
                nextUrl = url[0: url.rfind("_")] +"_"+ str(int(url[url.rfind("_")+1 : url.rfind(".")])+1)+".htm"
                analysisAndWriteUrl(nextUrl)
            else:
                nextUrl = url[0: url.rfind(".")] + "_2" + ".htm"
                analysisAndWriteUrl(nextUrl)
        else:
            return
    except Exception as e:
        util.log(str(e))

def WriteImgUrlToFile(url):
    f = open("source\\美少女.txt", "a+")
    f.write(url)
    f.write("\n")
    f.close()

def bubbleDownload(url):
    res = requests.get(url, headers = headers)
    if res.status_code == 200:
        try:
            res.encoding = 'utf8'
            soup = BeautifulSoup(res.text, 'html.parser')
            lists = soup.select('.TypeBigPics')
            if len(lists) > 0:
                for item in lists:
                    analysisAndWriteUrl(item["href"])
        except Exception as e:
            util.log(str(e))
        if "_" in url:
            nextUrl = url[0: url.rfind("_")] +"_"+ str(int(url[url.rfind("_")+1 : url.rfind(".")])+1)+".htm"
            bubbleDownload(nextUrl)
        else:
            nextUrl = url[0: url.rfind(".")] + "_2" + ".htm"
            bubbleDownload(nextUrl)

if __name__ == "__main__":
    bubbleDownload("http://www.umei.cc/tags/meishaonv.htm")
    # url = ""
    # lists = [url]
    # while url != "exit":
    #     url = input("enter:")
    #     if lists.count(url) == 0:
    #         lists.append(url)
    #         analysisAndWriteUrl(url)
    # start = 188200
    # end = 200000
    # util.log("Download From " + str(start) + " to " + str(end))
    # for i in range(start, end):
    #     try:
    #         print(i)
    #         url = "http://www.umei.cc/p/gaoqing/gangtai/"+str(i)+".htm"
    #         #url = "http://www.umei.cc/meinvtupian/rentiyishu/"+str(i)+".htm"
    #         if fetchUrl(url):
    #             analysisAndWriteUrl(url)
    #     except Exception as e:
    #         util.log("Failed for" + str(i) + str(e))