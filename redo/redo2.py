#this will be for pandas and numpy
import numpy as np

np.__version__

#matrix can contain symbols or expressions
# matrix are set as:
#  A = [[a11,a12,a13,a14...a1n],[a21,a22,a23,a24...a2n], ..., [am1, am2, am3 ,am4...amn]]
# scalars are what you call a matrix element that has only one row and column (these are also one dimension)
# vectors are the colums in a matrix
# there are row vectors or column vectors
# matrix have n amount of columns and n amount of rows
# scalar is like a point in a graph, a vector as a linear, and matrix as two lines crossing each other

#to declare a scalar, vecto and matrix we do:
scalar = np.array(5)
vector = np.array([5,-2,4])
maxtrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

# we can get the shape or dimension by using shape:
print(maxtrix.shape)
print(vector.shape)

# we can use reshape to add a row or column
print(vector.reshape(1,3)) # this will return a reshaped row vector
print(vector.reshape(3,1)) # this will return a reshaped column vector

#tensor flow: they are what we have been discussingh which are the different dimensions but there is a rank 3 tensor after the matrix where its a collection of matrixes 
#we can create a tensor rank 3 by combining two matrices
m1 = np.array([[5,12,6], [-3,0,14]])
m2 = np.array([[9,8,7], [1,3,-5]])

t = np.array([m1, m2])
print(t.shape)

#to manually create a tensor we do:
t_masnual = np.array([[[5,12,6], [-3,0,14]], [[9,8,7], [1,3,-5]]])

print(t_masnual.shape)

#adding and subtracting matrixes wortks with any type including floats, vectors, and scalars
#  The matrices with different dimensions cannot be added or subtracted as matrix can be added only if there is element corresponding to every element.
m3 = m2+m1
m4 = m2-m1
print(m3)
print(m4)

#there is an exception in matrices shewr we can add matrices or vectors to a scalar and it would work:
print('original\n', m1)
print('plus one\n', (m1 + 1))

# we can also try to add a scalar set as an array instead of an int
m1+np.array([1])

# we can create a column to a row by using transposing verctors and vise versa, this changes the shapes not the values
#to transpose we do .T
print('before transpose:\n', m1)
print('after transpose\n', m1.T)

#Dot product of vectors are thes sum of the products of the corresponding elements, so the total of the products
x = np.array([2,8,-4])
y = np.array([1,-7,3])

print(np.dot(x,y)) #every index gets multiples to its opposite then added together so ex: 2*1 = 2 + (8*-7 =) -56 + -4*3 = -12 so its 2 + -56+-12 = -66 which is what dot did in the above example

#if we were to multiply a scalar to a scalar it will just multiply each other because there is no opposing to add after multiplying

np.dot(5,6) #this will give us 30

# matrix multiplication: we can multiple a matrix to a scalar as well as multiply a matrix to a matrix by using the dot product but the matrix of mxn can only be multiplied with a matrix of nxk so if we have a matrix of 3x2 we can multiply a matrix of 2xk 
# second dimension of first matrix must match first dimension of second matrix
# so mxn * nxk = mxk 
# when doing the dot product we always multiply a row vector with a column vector, its as it sounds, we match then side by side, multiply then add then together

# we can also do axis where axis 1 is the row and the axis 0 is rows
array_hw_2 = np.array([[4,5],[7,10]])
np.mean(array_hw_2, axis = 1) #will find the mean of all the rows 









