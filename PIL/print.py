#-*-coding:utf-8-*-

from PIL import Image
import sys, os

#定义素描函数,img为Image对象，
#threshold为阈值，介于0到100之间
def sketch(img, threshold):
	if threshold < 0:
		threshold = 0
	if threshold >100:
		threshold = 100
	width,height = img.size
	#将图片转化为灰度图
	img =img.convert('L')
	#将图片转化为像素矩阵
	pix = img.load()
	for w in range(width):
		for h in range(height):
			if w == width-1 or h==height -1:
				continue
			src = pix[w,h]
			dst = pix[w+1,h+1]

			diff = abs(src-dst)
			if diff >= threshold:
				pix[w,h]=0
			else:
				pix[w,h]=255
	return img

if __name__ =='__main__':
	#os.path.dirname(__file__)在脚本是以完整路径被运行的， 
	#那么将输出该脚本所在的完整路径
	#所在脚本是相对路径运行的，将输出空目录
	#以下两周方式拼接路径都可以
	#path = os.path.dirname(__file__) + os.sep.join(['', 'imanges', 'lam.jpg'])
	path = os.path.join(os.path.dirname(__file__), 'images','lam.jpg')
	print(path)
	threshold = 15

	if len(sys.argv) == 2:
		try:
			threshold = int(sys.argv[1])
		except ValueError:
			path = sys.argv[1]
	elif len(sys.argv) == 3:
		path = sys.argv[1]
		threshold = int(sys.argv[2])

	img = Image.open(path)
	img = sketch(img, threshold)
	img.save(os.path.splitext(path)[0]+'.sketch.jpg','JPEG')



