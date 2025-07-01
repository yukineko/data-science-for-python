import numpy as np
import numpy.random as random
data = np.array([1,2,3,4,5])
print(data)
print('Dataの型', data.dtype)
print('次元 ', data.ndim)
print('要素数 ', data.size)

data2 = data * 2
print(data2)
data3 = data2 * data
print(data3)
data[::-1].sort()
print(data)
print(data.cumsum())
print(data.sum())
print(random.choice(data, size=3)) # 重複あり
print(random.choice(data, size=3, replace=False)) # 重複なし

array1 = np.arange(9)
print(array1)
print(array1.reshape(3, 3)) # 3行3列に変形
array1 = array1.reshape(3, 3)
print(array1[0,:]) # 1行目の要素を表示
print(array1[1,:]) # 2行目の要素を表示
print(array1[:,0]) # 1列目の要素を表示

array2 = np.arange(9,18).reshape(3, 3)
print(array2)
print(np.dot(array1, array2)) # 行列の積
print(array1 @ array2) # 行列の積（@演算子）
print(array1 * array2) # 


print(np.zeros((2,3), dtype=np.int64)) # 2行3列のゼロ行列
print(np.ones((3,3), dtype=np.float64))

print(np.arange(1, 51).sum())
print(random.randn(10))
ns = random.randn(10)
print(ns, ns.max(), ns.min(), ns.mean(), ns.std(), ns.sum())
three = np.ones((5,5), dtype=np.int64) * 3
print(three @ three)