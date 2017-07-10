#some useful function
#im=Image.open('1.jpg')
#imload=im.load()
#imload[i,j] can show the RGB of pixel
#i,j=im.size can get the picture size
from PIL import Image
from PIL import ImageFilter as imagefilter

im=Image.open('2.jpg')
im=im.filter(imagefilter.SHARPEN)
im=im.filter(imagefilter.EDGE_ENHANCE)
im=im.filter(imagefilter.EDGE_ENHANCE_MORE)
imload=im.load()
im_w,im_h=im.size
for i in range(0,im_w-1):
	for j in range(0,im_h-1):
		a,b,c=imload[i,j]
		imload[i,j]=(255-a,255-b,255-c)
im.save('450.jpg')
