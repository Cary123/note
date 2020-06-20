# coding=utf-8
import os
def replaceSpecificWord(oldContent):
    newContent = oldContent.replace('<！', '<!')
    return newContent

def readFrom(path) :
    f = open(path, "r", encoding='utf-8')
    text = f.read()
    f.close()
    return text

def WriteTo(path, content):
    f = open(path, "a+", encoding='utf-8')
    text = f.write(content)
    f.close()

if __name__ == "__main__":
    sourceDir = r"H:\自媒体\文章\英文\new"
    targetDir= r"H:\自媒体\文章\英文\html"
    fileLists = os.listdir(sourceDir)
    for item in fileLists:
        sourceFile = os.path.join(sourceDir, item)
        targetFile = os.path.join(targetDir, item)
        content = readFrom(sourceFile)
        content = replaceSpecificWord(content)
        WriteTo(targetFile, content)