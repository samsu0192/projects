#this is a script to test convert from png to jpeg

from PIL import Image
from PIL import ImageFilter
im=Image.open('image2.png')
rgb_im=im.convert('RGB')
rgb_im=rgb_im.filter(ImageFilter.SHARPEN)
rgb_imload=rgb_im.load()
im_w,im_h=im.size
'''
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		if rgb_imload[i,j]==(0,0,0):
			rgb_imload[i,j]=(100,100,100)   
for i in range(0,im_w-1):
	 for j in range(0,im_h-1): 
		if rgb_imload[i,j]!=(100,100,100):
			rgb_imload[i,j]=(0,0,0)
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		if rgb_imload[i,j]==(100,100,100):
			rgb_imload[i,j]=(255,255,255)
'''
'''
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		x,y,z=rgb_imload[i,j]
		rgb_imload[i,j]=(255-x,255-y,255-z)
		'''
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		x,y,z=rgb_imload[i,j]
		if rgb_imload[i,j]==(255,255,255) or rgb_imload[i,j]==(0,0,0):
			rgb_imload[i,j]=(255-x,255-y,255-z)
rgb_im=rgb_im.filter(ImageFilter.EDGE_ENHANCE_MORE)
rgb_im.save('image345.jpg')
