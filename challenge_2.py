import numpy as np # imported library
import matplotlib.pyplot as plt # imported library

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1]) # array
bins = np.array([0, 1, 2, 3]) # histogram blocks

print("\nNumbers: ", nums) # to print the numbers
print("\nBins: ", bins) # to print the bins (blocks)
print("\nResult", np.histogram(nums, bins)) # to print the results

plt.hist(nums, bins=bins, color="skyblue") # to initialize the graph
plt.title("Histogram") # title of graph
plt.show() # to close the program
