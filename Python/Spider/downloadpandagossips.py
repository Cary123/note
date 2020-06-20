import urllib,re,requests
import sys
import util
import json
import os
from bs4 import BeautifulSoup

headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

loveList = ['爱', '性', '男', '女', '吻', '分手', '挽回', '对象', '上床', '结婚', '老婆', '丈夫', '怀孕']

#check file existed or not, create file
def checkAndCreateFileForWriteTitle(path, title):
    if (not os.path.exists(path)):
        fo = open(path, "a+")
        fo.write('\t\t\t'+title+"\n")
        fo.close()
        return True
    else:
        return False

# Write second level title
def WriteSecondLevelTitle(path, secondLevelTitle):
    fo = open(path, "a+")
    fo.write(secondLevelTitle+"\n")
    fo.close()

# Write content
def WriteContent(path, content):
    fo = open(path, "a+")
    fo.write(content+"\n")
    fo.write(" \n")
    fo.close()

# Parse video info by url
def parseArticleInfoByUrl(url):
    try:
        r = requests.get(url, headers = headers)
        res = requests.get(url)
        if res.status_code == 200:
            res.encoding = 'utf8'
            soup = BeautifulSoup(res.text, 'html.parser')
            titlelists = soup.select('header .p-article__title')
            contentlists = soup.select('.p-article__detail div')
            if len(titlelists) > 0:
                try:
                    title = util.translate(titlelists[0].text)
                    title = re.sub('[\/:*?"<>|]','-',title)
                    path = "H:/自媒体/文章/"+title+'.txt'
                    for subText in loveList:
                        if subText in title:
                            path = "H:/自媒体/文章/情感/"+title+'.txt'
                            break
                    if checkAndCreateFileForWriteTitle(path, title):
                        util.log("Write:" + url)
                        for item in contentlists:
                            if item.has_attr('class'):
                                if item.attrs['class'][0] == 'p-article__heading':
                                    secondLevelTitles = item.select('h2')
                                    if len(secondLevelTitles) == 0:
                                        secondLevelTitles = item.select('h3')
                                    if len(secondLevelTitles) > 0 and len(secondLevelTitles[0].find_all(lambda x: x.name != '', recursive=False)) == 0:
                                        WriteSecondLevelTitle(path, str(secondLevelTitles[0].text))
                                elif item.attrs['class'][0] == 'p-article__text':
                                    contents = item.select('p')
                                    if len(contents) > 0 and len(contents[0].find_all(lambda x: x.name != '', recursive=False)) == 0:
                                        WriteContent(path, str(contents[0].text))
                except Exception as e:
                    util.log("Failed request:" + url)
                    util.log(str(e))
    except Exception as e:
        util.log("Failed request:" + url)
        util.log(str(e))

if __name__ == "__main__":
    for i in range(167, 4000):
        parseArticleInfoByUrl("https://pandagossips.com/posts/"+str(i))
        print("Downloaded:"+str(i))
