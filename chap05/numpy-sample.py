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
