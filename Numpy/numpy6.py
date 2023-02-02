import numpy as np

list_a = [[1,2,3],[4,5,6]] # a list of lists
print(type(list_a))

array_a = np.array(list_a)
print(type(array_a))

#if we do len() for list_a it will tell us as an overview of the list amount which would be 2 but if we want to know the sublist or inner list then we have to give it the position of the one we are talking about
print(len(list_a[0]))

#remember: lists concadenate when adding while arrays calcualte them since narrays are used for operations