# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('example2.jpg')
Z = img.reshape((-1,3))
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

im = cv2.imread('data/src/lena.jpg')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8

im[:, :, (0, 1)] = 0

cv2.imwrite('data/dst/lena_opencv_red.jpg', im)

"""
Spyder Editor

This is a temporary script file.
"""