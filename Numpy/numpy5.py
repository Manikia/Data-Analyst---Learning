import numpy as np

#ndarray is able to store multiple numeric values in a sequence and havs elementwise properties
#n is set as the natural number\
array_a = np.array([1,2,3])
#array is the name of the array we are creating but the array_a is the ndarray object of the array

print(array_a)

array_b = np.array([[4,5,6], [7,8,9]])
print(array_b)

array_c = np.array(13)

print(type(array_c))

#if we do an np.array with no brackets and one digit then it will have no dimension and be a 0 dimension but if we do a single integer inside a bracjet it will create a 1 dimension bracket
