import numpy as np

# 1
lst = [12.23, 13.32, 100, 36.32]
arr_1d = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr_1d)

# 2
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3)

# 3
null_vec = np.zeros(10)
print(null_vec)
null_vec[6] = 11
print("Update sixth value to 11", null_vec)

# 4
arr_12_38 = np.arange(12, 38)
print(arr_12_38)

# 5
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype(float)
print("Original array", arr_int)
print("Array of floats", arr_float)

# 6
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# 8
arr_rand_10 = np.random.rand(10)
mean_val = np.mean(arr_rand_10)
median_val = np.median(arr_rand_10)
std_val = np.std(arr_rand_10)
print("Random array:", arr_rand_10)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)
# 9
arr_10x10 = np.random.rand(10, 10)
print("Min:", arr_10x10.min())
print("Max:", arr_10x10.max())

#10
arr_3x3x3 = np.random.rand(3, 3, 3)
print(arr_3x3x3)
