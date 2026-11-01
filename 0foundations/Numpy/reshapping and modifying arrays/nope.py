import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)

new_arr_2d = np.insert(arr_2d,0,[1,2,5],axis=0)#inserting a new row at the beginning of the array and if axis = none it will insert the values in the flattened array
print(new_arr_2d)