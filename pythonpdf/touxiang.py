#coding:utf-8
# 引入Pillow测试正常，给头像加数字

from PIL import Image, ImageDraw, ImageFont, ImageColor
import os
import sys
if __name__ == "__main__":
    filename = os.path.abspath(__file__)
    dirname=os.path.dirname(filename)
    imgname=os.path.join(dirname,"touxiang.jpg")
    im = Image.open(imgname)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    font0 = ImageFont.truetype("symbol.ttf", size=40)
    font1= ImageFont.truetype("symbol.ttf", size=20)
    fillColor = ImageColor.colormap.get("black")
    draw.text((width - 125, 0), "遇见你\n 真好", font=font0, fill=fillColor)
    draw.text((width - 125, 0), "\n\n\n\n   —刀刀女孩", font=font1, fill=fillColor)
    im = im.convert('RGB')
    im.save("python.jpg")
