import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
o = np.delete(arr, 3 , axis = 0)
print(o)

arr_2d = np.array([[4,5,3,2],[1,2,3,4]])
p = np.delete(arr_2d, 1, axis=0)  # Deleting the second row
print(p)