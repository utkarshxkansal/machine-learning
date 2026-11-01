import numpy as np
arr = np.array([10,20,30,40,50,90])
reshaped_arr = arr.reshape(2,3)
# print(reshaped_arr)

# reshapping never creates a copy of the data it creates view


#flattening array
print(reshaped_arr.flatten())
print(reshaped_arr.ravel())
bath = reshaped_arr.ravel()# ravel also flattens the array but it returns a view of the original array
flat = reshaped_arr.flatten()# flatten returns a copy of the original array
bath[0] = 145
flat[0] = 100
print(bath)   
print(flat)


print(reshaped_arr)

