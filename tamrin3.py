import cv2
import numpy as np

# part_1
# image=cv2.imread('image/building.tif',cv2.IMREAD_GRAYSCALE)
# mask=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# result=np.zeros((600, 600),dtype='int8')
# print(image.shape)
# rows,cols=image.shape
# for i in range(1,rows-1):
#     for j in range(1, cols - 1):
#         small_image=image[i-1:i+2,j-1:j+2]
#         besco = np.multiply(small_image,mask)
#         out=np.sum(besco)
#         result[i,j]=out
# cv2.imshow('out',result)
# cv2.imwrite('out1.jpg',result)
# cv2.waitKey()


# part_2
image=cv2.imread('image/building.tif',cv2.IMREAD_GRAYSCALE)
mask=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
result=np.zeros((600, 600),dtype='int8')
print(image.shape)
rows,cols=image.shape
for i in range(1,rows-1):
    for j in range(1, cols - 1):
        small_image=image[i-1:i+2,j-1:j+2]
        besco = np.multiply(small_image,mask)
        out=np.sum(besco)
        result[i,j]=out
cv2.imshow('out',result)
cv2.imwrite('out2.jpg',result)
cv2.waitKey()