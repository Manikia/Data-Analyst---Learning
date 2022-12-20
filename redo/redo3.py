#intro to pandas
import pandas as pd
import numpy as np

products = ['A','B','C','D']

#to turn into a series we do:
product_categories = pd.Series(products)

print(product_categories)

array = np.array([10,20,30,40,50])

series_a = pd.Series(array)

print(series_a)

# pandas series should be used when working with larger tools and capabilities where pandas can be used as well
#series have explicit indexes for the objects it stores since it stores in sequential order
# with series we should keep data of single types

#attributes is a variable providing metadata about an object
#methods is an function that can be associated with an object

#type of attributes:

print(series_a.dtype) #shows type
print(series_a.size) #shows size of series

#object type is defined to all numeric data in python
#when we identify a variable series its not the name of the series that will show in the ouitput of our code, instead we would have to define the name for it:
product_categories.name = 'Product Categories'
print(product_categories.name)
#attributes help us extract information but not modify them

prices_per_category={'Product A': 22250, 'Product B': 16600, 'Product C': 15600}
prices_per_category = pd.Series(prices_per_category)
print(prices_per_category.index) #helps you see the index position 
print(prices_per_category.index[1]) #if we do this we can see the specific details based on the index we look for

#label based vs position based indexing
print(list(series_a))
print(series_a.index)

#explicit indexing is when we define the object to the index and valu like we did in prices per category but implicit is when we dont define the index then it will create a zero based index like when we create a sequence nad it starts at 0- wahtever number thats implicit indexing but expliti is when we name the indexes

#we can set the index names like in prices per category or like below:
series_b = pd.Series([10,20,30,40,50], index = [1,2,3,4,5])
print(series_b[2])

print(series_b.idxmax())#returns the highest value in a series while idxmin finds the smallest

#working with numeric data is better to use numpy but with both numeric and non numeric its better with pandas
#to get the beginning 5 rows we do .head() but to get the last 5 rows we do .tail() but we can also add a number in the parenthesis/argument to return us a specific amount 




