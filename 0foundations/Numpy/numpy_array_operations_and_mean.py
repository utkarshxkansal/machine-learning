import numpy as np
arr = np.array([40,31.9,55.9])
average = np.mean(arr)
print("The average of the array is:", average)
# instead of np.mean(arr) we can directly write arr.mean() cuz python already knows it belongs to np 
print(arr.mean())

# ans is same we can check

 

# numpy is faster and consume less meamory and has easy maths operations
list = [1,2,3,4,5]
print(list)
array = np.array(list)
print(array)
print(arr.astype(str))

import numpy as np
arr = np.array([1, 2, 3])
print(arr+4)
print(arr*2)
print(arr-1)
