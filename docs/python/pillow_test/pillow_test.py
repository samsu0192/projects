#some useful function
#im=Image.open('1.jpg')
#imload=im.load()
#imload[i,j] can show the RGB of pixel
#i,j=im.size can get the picture size
from PIL import Image

im=Image.open('1.jpg')
imload=im.load()
im_w,im_h=im.size
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		if imload[i,j]==(0,0,0):
			imload[i,j]=(255,255,255)	
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		if imload[i,j]!=(255,255,255):
			imload[i,j]=(0,0,0)
im.save('10.jpg')
