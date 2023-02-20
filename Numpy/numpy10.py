import numpy as np

#np.empty() creates an empty np array of a shape and type, it returns the array without initializing entries, its the fastest way to generate an array

array_empty = np.array(shape = (2,3)) #this will create an empty array but with dimensions since technically we cant create empty arrays in programming(Return a new array of given shape and type, without initializing entries.)
#the bad thing about the above is that it takes memory allocation but instead we could just creaste an arrau where it is slower but more consistent

array_zero = np.zeros(shape = (2,3)) #Return a new array of given shape and type, filled with zeros.

#the difference between empty and zeros is that empty might just add jubberish whilst the zero one will actually create 0 inside the empty array
#we can also initialize the dtype 

#np.one() is the same as np.zero, works the same way
array_one = np.ones(shape = (2,3))

#np.full() fills the array with the value we tell it which takes a scalar value of fill_value
array_full = np.full(shape = (2,3), fill_value = 2)
#the fill_value takes a scalar value meaning it can take in numbers or strings so we can set the fill_value = 'test' and it will replace all the spaces of the shape with 'test'

#_like functions we dont need to specifiy the shape and instead we provide antoher array anbd the function will automatically take the shape and type of it

matrix_a = np.array([[1,0,9,2,2],[3,23,4,5,1],[0,2,3,4,1]])

empty_like = np.empty_like(matrix_a) #it works the same with empty, ones and full

#with zero like it will take the shape the same way but comparting w empty and zeros it will always be 0s never any other int unlike empty
matrix_b = np.array([[1,0,9,2,2],[3,23,4,5,1],[0,2,3,4,1]])

zeros_like = np.zeros_like(matrix_b) 