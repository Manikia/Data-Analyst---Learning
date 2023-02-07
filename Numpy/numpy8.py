#slicing
import numpy as np

matrix_A = np.array([[1,2,3],[4,5,6]])
#slicing is creating a new array from getting a chunk of values from an existing one

matrix_A[:] #this means that we are indexing the interval of all values since we didnt specify anything
print(matrix_A[0:1]) #this is saying start at index 0 and end before 1 so itll be 0,0 the first row
print(matrix_A[:,:])
print(matrix_A[1:2,1:2]) #the first : is the row and the other is the column

print(matrix_A[0:2,1:2])

#slices are basically smaller arrays
#indexing = specific indexing
#slicing = interval indexing

#stepwise slicing is when we take steps to slice in an array
matrix_B = np.array([[1,1,1,2,0],
                     [3,6,6,7,4],
                     [4,5,3,8,0]])

print(matrix_B[::,0:3:2]) #it follows start:end:step

#if we do a step of -1 then it will go through the array backwards so it will start from the bottom of the matrix and go up
print(matrix_B[::-2,::2]) #this will go backwards from the end since we are doing -2 and it will continue 

print(matrix_B[::-1,::2]) #it just goes backwards but keeps its form

#conditional slicing
matrix_C = np.array([[1,1,1,2,0],[3,6,6,7,4],[4,5,3,8,0]])
#we can add conditions in our sliced arrays as well
print(matrix_C[:,0] >2)

#if we want a value returned of a condition we can do
print(matrix_C[matrix_C[:,:] > 2])
#treats the entire matrix as a 1D array