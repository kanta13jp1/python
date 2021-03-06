# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(12) # １つ１次元配列を生成。

print(a)

b = np.reshape(a, (3, 4)) # 3×4の２次元配列に変形。

print(b)

b[0, 1] = 0

print(b)

print(a)

c = np.arange(12) # もう一度同じ配列を生成。

d = np.reshape(c, (3,4), order = 'C') # orderを設定することで、並べ替え方を設定できる。

print(d)

d = np.reshape(c, (3,4), order = 'F') # ここを'F'にすると高い次元のindexがまず変化していくように変形される。

print(d)

a = np.arange(24) #　もう一度配列を生成。

b = np.reshape(a, (3,-1))   # (n, -1)と`shape`を指定するとn×m (mは配列の要素数に合わせた値)の配列を返す。

print(b)

b = np.reshape(a, (-1,6))   # (n, -1)と`shape`を指定するとn×m (mは配列の要素数に合わせた値)の配列を返す。

print(b)

a = np.arange(12).reshape((3, 4))

print(a)

b = np.arange(12).reshape((3,-1))  # -1も使える。

print(b)

