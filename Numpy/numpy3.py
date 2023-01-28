import numpy as np

array_a = np.array([[1,2,3], [4,5,6]], dtype = 'float32') #we can set the array of a type by doing dtype
array_a = np.array([[1,2,3], [4,5,6]], dtype = np.complex64) #or we can also do it this way

array_a = np.array([[1,2,3], [4,5,6]], dtype = np.bool_)
print(array_a)

array_a = np.array([[1,2,3], [4,5,6]], dtype = np.str_)
print(array_a)

