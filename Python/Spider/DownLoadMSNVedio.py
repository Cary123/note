import urllib,re,requests
import sys
import util
import json
import os
from bs4 import BeautifulSoup

routes = ['https://www.msn.com/en-ca/video/superbowl',
'https://www.msn.com/en-ca/video/animals',
'https://www.msn.com/en-ca/video/diyandrecipes',
'https://www.msn.com/en-ca/video/autos',
'https://www.msn.com/en-ca/video']
urlCollection = []
# If failed hit for 3 times, break
MaxFailedHit = 5

headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
 'Cookie':'MUID=0DA4D4BD498D6CFB3AA9D9BE4D8D6820; _SS=SID=00; videoCookiesLastCategory=en-ca=animals; _cb_ls=1; _cb=DsAPZCJmzJ0BiCB2c; _chartbeat2=.1550504320201.1550509083431.11.uAsG96ZMUeDgWcawC2JWWNCmna0Z.1; ANON=A=E43533FD3C93526D33F4F5C4FFFFFFFF&E=164d&W=1; NAP=V=1.9&E=15f3&C=gBm5NGQ6hq9_2JLke_9M_uUX-nhzUVJp3UwliRTchLXC4pE05Iv2DA&W=1; vidvol=10; adoptout={"msaOptOut":0,"adIdOptOut":0}; videoerrorcount=0; trg=0%7C0%7C0; ecasession=v2_9a22cfec7b49fc3893239e7b074a63fd_ba74fcd1-eff2-48d8-b6af-082423d58358-tuct35eea8e_1550666026_1550666984_CNawjgYQqLw-GP6e37rd9J7zBiACKAYwMDjK_QdA_qAQSI7OHlCJxAlYAGAC'
}

# Parse video info by url
def parseVedioInfoByMSNUrl(url):
    r = requests.get(url, headers = headers)
    res = requests.get(url)
    if res.status_code == 200:
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, 'html.parser')
        lists = soup.select('.video-info script')
        nextVideoList= soup.select(".videoplaylist ul li a")
        videoInfo = None
        if len(lists) > 0:
            try:
                videoInfo = json.loads(lists[0].text)
            except:
                util.log("failed found:" + lists[0].text)
        if len(nextVideoList) > 0 and videoInfo is not None:
                videoInfo["nextUrl"] = nextVideoList[0]["href"]
        return videoInfo

#check and download video
def downloadVideo(url, path):
    if (not os.path.exists(path)):
        urllib.request.urlretrieve(url, path)

#check file existed or not, create file
def checkAndCreateDescFile(path, title, desc):
    if (not os.path.exists(path)):
        fo = open(path, "a")
        fo.write(desc)
        fo.close()


# check folder existed or not, if not create it
def checkAndCreateFolder(folderName):
    if (not os.path.exists(folderName)):
        os.makedirs(folderName)

# handle video by videoinfo
def handleVideoInfo(videoInfo):
    try:
        # Create video folder
        videoDir = "H:\\自媒体\\2019-02"
        # + videoInfo['uploadDate'][:10]
        checkAndCreateFolder(videoDir)   
        # Translate name and description
        name = util.translate(videoInfo['name'])
        desc = util.translate(videoInfo['description'])
        url = videoInfo['contentUrl']
        duration = videoInfo['duration']
        videoPath = videoDir + "\\"+name+".mp4"
        descPath = videoDir + "\\" + name + ".txt"
        #download video
        downloadVideo(url, videoPath)
        # write desc
        checkAndCreateDescFile(descPath, name, desc)
    except:
        util.log(json.dumps(videoInfo))

def changeRoute(routeNum):
    if routeNum < len(routes):
        return routes[routeNum]

if __name__ == "__main__":
    """
    {
        "description":"February 12, 2019 - San Diego Zoo Global researchers have confirmed the presence of rare black leopards living in Laikipia County, Kenya.",
        "name":"Remote cameras confirm rare black leopards living in Kenya",
        "thumbnailUrl":"https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBTtKCU.img",
        "uploadDate":"2019-02-11T19:17:49.0000000Z",
        "contentUrl":"http://wus-streaming-video-msn-com.akamaized.net/00e33de7-0746-439d-b75c-f096dd282f18/f4518be8-e342-4def-9197-9ba0b459_2250.mp4",
        "duration":"PT33S",
        "expires":"2020-02-12T14:58:17.0000000Z",
        "@context":"http://schema.org",
        "@type":"VideoObject"
    }
    """
    failedHit = 0
    initurl = "https://www.msn.com/en-us/video/animals/the-most-adorable-hedgehogs/vi-BBTR6KW"
    urlCollection.append(initurl)
    while failedHit < MaxFailedHit:
        try:
            videoInfo = parseVedioInfoByMSNUrl(initurl)
            handleVideoInfo(videoInfo)
            initurl = videoInfo["nextUrl"]
            if (initurl in urlCollection):
                initurl = changeRoute(failedHit)
                failedHit = failedHit + 1
            else:
                urlCollection.append(initurl)
        except:
                initurl = changeRoute(failedHit)
                failedHit = failedHit + 1
