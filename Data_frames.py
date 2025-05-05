#Libraries: Pandas, Numpy, Matplotlib, Seaborn
#step 1: Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Numpy basics: Arrays and math
print("NumPy Arrays and Math Operations")

#Create an array/s
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print("Array arr1:",arr1)
print("Array arr2:", arr2)

#Operations (subtraction, addtion, division)
print("Addtion", arr1+arr2)
print("Multiplication:", arr1*arr2)
print("Mean:",np.mean(arr2))
print("Square root of:", np.sqrt(arr1))