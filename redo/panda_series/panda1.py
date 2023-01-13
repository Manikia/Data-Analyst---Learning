import pandas as pd

data = pd.read_csv('./redo/csv_files/Location.csv', squeeze = True) #reformatting the series 
location_data = data.copy() #we are copying the data to new variable location_data

#we can then look at the data that we have by using describe:
print(location_data.describe())

#there are two different unique methods we can use to look at our data
#.nunique() will return the amount of unique data we have while
#.unique() will return what unique data we have

#converting series into arrays
import numpy as np

prices = pd.Series({'Product A': 22250, 'Product B':16600, 'Product C': 15600}) #series
#if we want ot see the values of our series we can do:
print(prices.values)
print(prices.array)
print(prices.values[0])
print(type(prices.array)) #in this case the array has been built on top of the numpy series so if we want to create it where it isnt built on top and instead is an actual array we have to do, which will convert to an actual array:
print(prices.to_numpy())
print(prices.values[0])

#all thse ways will convert it to an array:
#.values .array and .to_numpy

#to organize the values of data from one or more columns we can do the below with sort_values:
numbers = pd.Series([15,1000,23,45,444])
print(numbers.sort_values(ascending = False))
#using sort_values we can sort NaN data to make it output first, string data, if we want the lowercase first or the uppercase, etc
#if we are working with strings it will organize by alphabetical

#to check the amount of attributes in a csv file we can do .index
#to check the name ofthe index data we do .name and if doesnt have one we can set it equal to the name we want to set the index as

location_data.name = 'Index'
print(location_data.index)

#remember how when we tried to sort we would only get the variables sorted not the index, well in this case we can sort the index only as well by doing: .sort_index() but the thing is that it is only a temporay manipulation and if we print it out it will be back to how it was
#we can sort both the index and variables the same if we use ascending and both sort_index(ascending = True)