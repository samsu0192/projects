"""
#matlab Version
B='imread'('1.png');
A=rgb2gray(B);
[m,n]=size(A);
for i=1:1:m
for j=1:1:n
if(A(i,j)>110)
A(i,j)=255;
end
end
end
imwrite(A,'1.jpg')
"""
#python version
from PIL import Image
col=Image.open(path_to_file)
gray=col.convert('L')
#convert RGB to Gray
wb=gray.point('lambda x:255 if x>110 else x')
wb.write('1.jpg')
