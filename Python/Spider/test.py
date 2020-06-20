import os
import random
import util
import time

def GenerateHtmlHeader():
    header= '''<!DOCTYPE html> \n
            <html lang="en"> \n
            <head> \n
                <meta charset="UTF-8"> \n
                <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n
                <meta http-equiv="X-UA-Compatible" content="ie=edge"> \n
                <title>Document</title> \n
            </head> \n
            <body> \n'''
    return header

def GenerateHtmlFooter():
    footer= ''' \n</body> \n
               </html> \n'''
    return footer

def GenerateContent(content, imgUrl) :
    htmlValue = content
    if len(content) < 30:
        htmlValue = "<p><strong>"+content+"</p></strong>"
    else:
        htmlValue = "<p>"+content+"</p>"
        i = int(random.random() * 20)
        if i%9 == 0:
            htmlValue = htmlValue + '<p><img src="'+imgUrl+'"/></p>'
    return htmlValue


def readFrom(path) :
    f = open(path, "r")
    text = f.readlines()
    f.close()
    return text

def WriteTo(path, content):
    f = open(path, "a+", encoding='utf-8')
    text = f.write(content)
    f.close()

def ReplaceDirtyData(dirtyData):
    clearData = dirtyData.replace('性生活','羞羞的生活').replace('性爱','男女关系').replace('做爱','做羞羞的事').replace('上床','做羞羞的事')
    return clearData

if __name__ == "__main__":
    sourceDir = r"H:\自媒体\文章\英文"
    targetDir= r"H:\自媒体\文章\英文\transfer"
    imgFile = r"F:\mayun\Note\Python\Spider\source\img.txt"
    fileLists = os.listdir(sourceDir)
    images = readFrom(imgFile)
    translateAPIDown = False
    for item in fileLists:
        #前任, 迹象,喜欢，想你，约会，关系, 伴侣
        if item.find(".") > 0 and (item.find("约会") > 0 or item.find("关系") > 0 or item.find("伴侣") > 0) and (item.find("迹象") < 0 and item.find("前任") < 0):
            print("transfer article:"+item)
            sourceFile = os.path.join(sourceDir, item)
            targetFile = os.path.join(targetDir, item+".html")
            contentlists = readFrom(sourceFile)
            content = GenerateHtmlHeader()
            i = 0

            for line in contentlists:
                line = line.replace("\n", "").strip()
                if len(line) > 0:
                    a = int(random.random()*500)
                    imgUrl = images[a].replace("\n","")
                    if i == 0 :
                        content = content + GenerateContent(line, "")
                    else:
                        time.sleep(3)
                        translateContent = util.translate(line)
                        if translateContent == "":
                            translateAPIDown = True
                            break
                        else:
                            translateContent = ReplaceDirtyData(translateContent)
                            content = content + GenerateContent(translateContent, imgUrl)
                i = i + 1
            content = content + GenerateHtmlFooter()
            if translateAPIDown:
                break
            WriteTo(targetFile, content)