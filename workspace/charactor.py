#-*-coding:utf-8-*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

#随机大写字母：
def rndChar():
	return chr(random.randint(65,90))
#随机颜色1:
def rndColor():
	return(random.randint(64,255), random.randint(64,255), random.randint(64,255))
#随机颜色2：
def rndColor2():
	return(random.randint(32,127), random.randint(32,127), random.randint(32,127))


#240*60
width = 60*4
height = 60
#Image.new(mode, size, color=None)
image = Image.new('RGB',(width,height), (255,255,255))
#创建Font对象
font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\SIMYOU.TTF',36)
# 穿件draw对象并和image绑定
#用于以后绘制像素点和文本
draw = ImageDraw.Draw(image)
#通过像素点绘制填充图片
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())

#绘制字母
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font=font, fill=rndColor2())
#模糊处理
#image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

