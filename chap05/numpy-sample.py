import numpy as np

sample_array = np.arange(10)
print(sample_array)

sample_array_slice = sample_array[0:3]
print(sample_array_slice)

sample_array_slice[0:3] = 10
print(sample_array_slice)
print(sample_array)

sample_array_cp = np.copy(sample_array)
print(sample_array_cp)
sample_array_cp[-3:-1] = 2
print(sample_array_cp)
print(sample_array)

print(sample_array_cp[3])

sample_array3 = np.array([[1,2,3],[4,5,6]])
sample_array4 = np.array([[7,8,9],[10,11,12]])
sample_array_vstack = np.vstack((sample_array3, sample_array4))
print(sample_array_vstack)

first,second,third = np.split(sample_array_vstack, [1,3])
print(first)
print(second)
print(third)

sample_array5 = np.array([[13,14,15],[16,17,18],[19,20,21]])
sample_array_vstack2 = np.vstack((sample_array3, sample_array4, sample_array5))
print(sample_array_vstack2)

first,second,third,forth = np.split(sample_array_vstack2, [2,3,5])
print("----------------------------")
print(first)
print(second)
print(third)
print(forth)
print("----------------------------")
print(first.repeat(5))

sample_array = np.arange(10)
print(sample_array + 3)

print("----------------------------")
sample_array1 = np.arange(12).reshape(3, 4)
sample_array2 = np.arange(12).reshape(3, 4)
print(np.vstack((sample_array1, sample_array2)))
print(np.hstack((sample_array1, sample_array2)))

sample_list = [1, 2, 3, 4, 5]
sample_array = np.array(sample_list)
print(sample_array + 3)