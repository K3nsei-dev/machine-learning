import numpy as np
from numpy import * # imported library
z = np.arange(20) # the array

print("The array is:") # to print the array
print(z)

z_mean = np.mean(z) # mean of the array
print("\nThe mean of the array is: ", z_mean)

z_std = np.std(z) # the standard deviation of the array
print("\nThe standard deviation of the array is: ", z_std)

z_var = np.var(z) # the variance of the array
print("\nThe variance of the array is: ", z_var)
