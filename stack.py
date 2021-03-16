# -*- coding: utf-8 -*-
import numpy as np

#a = np.arange(12)
#b = np.arange(2)

#print(a)

#print(b)

#c = np.hstack((a, b)) # 結合してみる。

#print(c)

#d = np.vstack((a, b)) # 結合してみる。

#print(d)

#c = np.arange(2).reshape(2, 1) # 2次元配列を作る。

#print(c)

#d = np.hstack((a, c)) # aとつなげてみるとエラーが返ってくる。

#print(d)

#d = np.arange(5).reshape(5, 1) # shapeを(1, 5)にする

#print(d)

#e = np.hstack((c, d)) # これなら結合できる。

#print(e)

#e = np.vstack((c, d)) # 結合してみる。

#print(e)

f = np.arange(12).reshape(2, 2, 3)

print(f)

g = np.arange(6).reshape(2, 1, 3) # 今度は3次元でやってみる。

print(g)

h = np.hstack((f,g))

print(h)

#i = np.vstack((f,g))

#print(i)