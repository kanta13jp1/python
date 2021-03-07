# -*- coding: utf-8 -*-
import numpy as np

rand = np.random.rand()  # 一つの乱数

print(rand)

arr = np.random.rand(3)  # サイズが3の配列の乱数

print(arr)

arr = np.random.rand(4, 4)  # 4 x 4の配列の乱数

print(arr)

arr = np.random.rand(3, 2, 2)  # 3 x 2 x 2の配列の乱数

print(arr)

rand = (1000 - 1) * np.random.rand() + 1

print(rand)