#Import NumPy as np

import numpy as np

# Create an array of 10 zeros

zeros = np.zeros(10)

# Create an array of 10 ones

ones = np.ones(10)

# Create an array of 10 fives

fives = np.ones(10) * 5

# Create an array of the integers from 10 to 50

int_arr = np.arange(10, 51)

# Create an array of all the even integers from 10 to 50

even_arr = np.arange(10, 51, 2)

# Create a 3x3 matrix with values ranging from 0 to 8

matrix = np.arange(9).reshape(3,3)
print(matrix)

# Create a 3x3 identity matrix

im = np.eye(3)

# Use NumPy to generate a random number between 0 and 1

num = np.random.rand(1)

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

new_array = np.random.randn(25)

# Create the following matrix (Jupyter Ntb)

new_array1 = np.arange(1, 101, 1).reshape(10, 10) / 100

# Create an array of 20 linearly spaced points between 0 and 1

lin_arr = np.linspace(0, 1, 20)

# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

mat = np.arange(1,26).reshape(5,5)
arr1 = mat[2:, 1:]
arr2 = mat[3, 4]
arr3 = mat[:3, 1:2]
arr4 = mat[4, :]
arr5 = mat[3:, :]

mat_sum = mat.sum()
mat_sd = mat.std()
mat_axis = mat.sum(axis = 0)