import numpy as np

# 1. Create a list of 5 numbers
numbers_list = [10, 20, 30, 40, 50]

# 2. Convert it into a NumPy array
numbers_array = np.array(numbers_list)

# 3. Calculate mean, max, sum
mean_value = np.mean(numbers_array)
max_value = np.max(numbers_array)
sum_value = np.sum(numbers_array)

# 4. Print the results clearly
print("Numbers:", numbers_array)
print("Mean:", mean_value)
print("Maximum Value:", max_value)
print("Sum:", sum_value)
