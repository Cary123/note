#coding=utf-8 
import os
import os.path #文件夹遍历函数  
import codecs
f = codecs.open('../Resources/all.txt', 'w', 'utf8')
#获取目标文件夹的路径
filedir = '../Resources'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    oneFile = codecs.open(filepath, 'r', 'utf8')
    #遍历单个文件，读取行数
    for line in oneFile.readlines():
        f.writelines(line)
    f.write('\n')
