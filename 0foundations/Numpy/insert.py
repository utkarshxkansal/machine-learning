import numpy as np 

arr = np.array([10, 20, 30, 40, 50, 60])
print(np.insert(arr, 3, 99)) 
# The insert() function takes three arguments: the array to insert into, the index at which to insert, and the value to insert. In this example, we are inserting the value 99 at index 3 of the array arr. The resulting array will be [10, 20, 30, 99, 40, 50, 60].
#for 1d u dont have to write axis but for 2d you do
list_2d = [[1,2,4],[34,54,9]]
arr_2d1 = np.array(list_2d)
arr_2d = np.array([[1,2,4],[34,54,4]])
print(arr_2d1==arr_2d)
print(arr_2d)
print(np.insert(arr_2d,2,[[3,4,5],[1,2,4]],axis=0))#inserting a new row at the end of the array



print(np.insert(arr_2d,2,[[3,4,5],[1,2,4]],axis=0))