#numpy is a powerful library for numerical computing in Python
# It provides support for arrays, matrices, and a wide range of mathematical functions
# to operate on these data structures.
#Many other libraries like pandas, scipy, and scikit-learn build on top of numpy

#numpy is written in C and Fortran, making it very fast for numerical operations

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Perform basic operations
# Addition
array_sum = array_1d + 10
print("Array after addition:", array_sum)

# Multiplication
array_product = array_1d * 2
print("Array after multiplication:", array_product)

# Calculate mean and standard deviation
mean_value = np.mean(array_1d)
std_deviation = np.std(array_1d)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)

# Reshape a 1D array to 2D
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped Array:\n", reshaped_array)

# Access elements
first_element = array_1d[0]
print("First element of 1D array:", first_element)