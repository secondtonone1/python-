#-*-coding:utf-8-*-

from PIL import Image, ImageFilter
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
#获取图片大小
w,h = im.size
print('Original image size : width:%d height: %d' %(w,h))

#图片缩放
im.thumbnail((w//2, h//2))

print('Resize image to: %dx%d' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('test2.jpg', 'jpeg')


# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

im2 = im.filter(ImageFilter.CONTOUR)
im2.save('contour.jpg','jpeg')
