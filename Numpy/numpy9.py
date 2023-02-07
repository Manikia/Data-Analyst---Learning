import numpy as np

matrix_D = np.array([[1,1,1,2,0],[3,6,6,7,4],[4,5,3,8,0]])

#if we do matrix[0,0] then it will return as an int but if we do matrix[0,0:1] it will return as an array
#[0,0] = scalar
#[0,0:1] = vector
#[0:1,0:1] = matrix

#to avopid the above sitations where the way we get our info might be differently we can use the squeeze method
#the squeeze method remoces all the unnecessary dimensions in an array like [[1]] as 1 we will get a single numeric value

print(matrix_D[0:1,0:1].squeeze())
print(matrix_D[1,0:1].squeeze())

#equivalent function to the above:
print(np.squeeze(matrix_D[0:1,0:1]))