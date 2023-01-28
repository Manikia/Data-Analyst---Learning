import numpy as np

#universal functins are like an extenstion of the elementwise operation
#universal function operates on ndarrays in an element by element to suport array broadcasting, type casting, and other features

array_a = np.array([1,2,3])
array_b = np.array([[1],[2]])
array_c = np.array([[1,2,3], [4,5,6]])

#remember how in elementwise we wouldnt do operations of different sizes, well with broadcasting we can do that where it stretches over the other to produce and output of the same shape

print(np.add(array_a, array_c)) #adds them up
print(np.add(array_b, array_c)) #it will stretch the array_b to be [1,1,1][2,2,2] untill it is the same length of the other array so that its able to add up

#we can onyl broadcast if there is at least one number in the array, if we can alter the array or if its the same size

#to typecast we get every element of an array and change it to a specific datatype
print(np.add(array_a, array_c, dtype = np.float64))
#we can only do organic numbers here because we are trying to add them up by using broadcasting but otherwise it would be able to convert to a string

# new_array = np.array(array_a, array_c, dtype = np.str_)
# print(new_array)

#running over an axis
print(np.mean(array_c, axis = 0)) #this will find the mean of every column in the array
#axis means it will return only the column of the array but if we do 1 it will return the mean of the row instead


