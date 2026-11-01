import numpy as np
list_1 = [2,2,3,4,5]
list_2 = [6,7,8,9,10]
arr_1 = np.array(list_1)
arr_2 = np.array(list_2)
print(np.hstack((arr_1, arr_2))) # Stacking along the first axis (rows)
print(np.vstack((arr_1, arr_2))) # Stacking along the second axis (columns)
# slitting
print(np.hsplit(arr_1,5)) # Split arr_1 into 5 equal parts along the first axis (rows)