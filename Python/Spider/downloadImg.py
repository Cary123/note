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

def download(url, path):
    if (not os.path.exists(path)):
        urllib.request.urlretrieve(url, path)

def readFrom(path) :
    f = open(path, "r")
    text = f.readlines()
    f.close()
    return text

# check folder existed or not, if not create it
def checkAndCreateFolder(folderName):
    if (not os.path.exists(folderName)):
        os.makedirs(folderName)

if __name__ == "__main__":
    imgFile = r"F:\mayun\Note\Python\Spider\source\img.txt"
    images = readFrom(imgFile)
    i = 1
    j = 139
    for item in images:
        targetDir= r"H:\自媒体\图片\umei"
        targetDir = os.path.join(targetDir, str(j))
        checkAndCreateFolder(targetDir)
        targetFile = os.path.join(targetDir, str(i)+'.jpg')
        download(item, targetFile)
        if i % 5 == 0:
            i = 0
            j = j +1
        i = i +1
