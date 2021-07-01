import cv2
import numpy as np
import argparse

my_parser=argparse.ArgumentParser()
my_parser.add_argument('--kernel_size', type=int)
args=my_parser.parse_args()

image=cv2.imread('image/person.jpg',cv2.IMREAD_GRAYSCALE)
mask=np.ones((args.kernel_size,args.kernel_size), dtype=float)/49
# result=np.zeros(image.shape,dtype='int8')
# print(image.shape)
# rows,cols=image.shape
# for i in range(1,rows-1):
#     for j in range(1, cols - 1):
#         small_image=image[i-1:i+2,j-1:j+2]
#         besco = np.multiply(small_image,mask)
#         out=np.sum(besco)
#         result[i,j]=out
result=cv2.filter2D(image,-1,mask)
cv2.imshow('out',result)
# cv2.imwrite('out3.jpg',result)
cv2.waitKey()
