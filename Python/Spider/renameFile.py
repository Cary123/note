# coding = utf-8
import os
if __name__ == "__main__":
    path = r"H:\自媒体\图片"#想要重命名所有文件存放的文件夹
    filelist = os.listdir(path)
    i = 10001
    for item in filelist:
        os.rename(os.path.join(path,item),os.path.join(path,(str(i)+'.jpg')))
        i += 1