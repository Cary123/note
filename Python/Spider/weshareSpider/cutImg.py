import cv2
import os
from PIL import Image

if __name__ == "__main__":
    sourcePathDir = r'H:\自媒体\图片\huaban\boards\cosplay\total'
    targetPathDir = r"H:\自媒体\图片\huaban\boards\cosplay\cut"#想要重命名所有文件存放的文件夹
    existlist = os.listdir(targetPathDir)
    filelist = os.listdir(sourcePathDir)
    for item in filelist:
        if item not in existlist:
            try:
                sourcePathFile = os.path.join(sourcePathDir,item)
                targetPathFile = os.path.join(targetPathDir,item)
                # 导入相关的库
                # 打开一张图
                img = Image.open(sourcePathFile)
                # 图片尺寸
                img_size = img.size
                h = img_size[1]  # 图片高度
                w = img_size[0]  # 图片宽度
                #print("w:"+ str(w) + ", h:"+ str(h))
                x = 0
                y = 0
                w = w
                h = h-h*0.08 if h < 7000 else h
                # 开始截取
                region = img.crop((x, y, x + w, y + h))
                # 保存图片
                region.save(targetPathFile)
            except Exception as e:
                print(item+" failed!")
                print(e)
                pass
            
