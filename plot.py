# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

#x = np.random.randint(25,100,25)
#y = np.random.randint(175,255,25)
#z = np.hstack((x,y))
#z = z.reshape((50,1))
#z = np.float32(z)
#plt.hist(z,256,[0,256]),plt.show()

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
#criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Set flags (Just to avoid line break in the code)
#flags = cv2.KMEANS_RANDOM_CENTERS

# Apply KMeans
#compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)

#A = z[labels==0]
#B = z[labels==1]

# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
#plt.hist(A,256,[0,256],color = 'r')
#plt.hist(B,256,[0,256],color = 'b')
#plt.hist(centers,32,[0,256],color = 'y')
#plt.show()

# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
#x = np.random.normal(50, 10, 1000)
 
# ヒストグラムを出力
#plt.hist(x)

#plt.hist(x, bins=16)

#plt.hist(x, range=(50, 100), bins=16)

#plt.hist(x, cumulative=True)

#plt.hist(x, bottom=30)
	
#plt.hist(x, log=True)

#plt.hist(x, rwidth=0.8)

#plt.hist(x, color="red")

#plt.hist(x, histtype="step")

#plt.hist(x, histtype="stepfilled")

#plt.hist(x, align="left")

#plt.hist(x, align="right")

#plt.hist(x, orientation="horizontal")

# 平均 20, 標準偏差 10 の正規乱数を1,000件生成
#y = np.random.normal(20, 10, 1000)
#plt.hist([x, y], histtype="barstacked")

#plt.hist([x, y], stacked=True)

#plt.hist([x, y], stacked=True, color=['#f46d43', '#66bd63'])

#plt.hist([x, y], stacked=False)

#labels = ['V1', 'V2']
#plt.hist([x, y], label=labels)
#plt.legend()

#plt.hist(z, bins=256, range=(0,256), label=labels, rwidth=0.8, log=True)
#plt.legend()

X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))

# convert to np.float32
Z = np.float32(Z)

# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]

# Plot the data
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()
