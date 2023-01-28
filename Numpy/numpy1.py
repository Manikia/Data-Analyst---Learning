import numpy as np

array_a = np.array([[1,2,3],[4,5,6]]) #2d array
print(array_a[0,0])
#if we want to get the last variable we have to do -1 since its equivilant to -0 = 0
print(array_a[0, -1])

#if we want to alter the element in an array we can do
array_a[0,2] = 9
print(array_a)

list_a = [8,7,8]
array_a = list_a
print(array_a)