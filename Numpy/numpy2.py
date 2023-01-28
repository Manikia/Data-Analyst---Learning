import pandas as pd
import numpy as np

array_a = np.array([7,8,9])
array_b = np.array([[1,2,3],[4,5,6]])

#Elementwise section where it means that we will distribute the mathematical operation through everything in an array
print(array_a+1)

#the purpose of lsits is to hold data but for arrays is to compute operations which means that if we get an array and we add two it will increase everything by two but if we get a list and add 2 it will add it to the end, not calculate it
list = [1,2,3]
list = list+[1]
print(list)

#if we want to add uptwo arrays we have to make sure its the same length(columns)
