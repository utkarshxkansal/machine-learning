# list1= [1,2,3]
# list2= [4,5,6]

# result = [x+y for x,y in zip(list1,list2)]
# print(result)

# its quite a simple method of python but it takes a lot of time when the list is large and it is not efficient so we can use numpy to do this in a more efficient way



# vectorisation
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 + arr2
print(result)
