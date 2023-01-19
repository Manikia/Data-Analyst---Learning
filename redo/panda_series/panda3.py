#dataframes
import pandas as pd
import numpy as np

#to look for our index we can do .index
#to look for our columns we can do .columns
#to look at both our rows and columns we do .axes
#to look at our metadatatype like the type of all of our columns types we do .dtype
#to look for our 2d array of our object we do .values and it will return a list of our data and its dimensions
#to convert a series or index to a numpy we do .to_numpy()
#to get the shape of an object we can do .shape it will be shown as (rows,columns)

#we can select data in pandas in two ways:

data = pd.read_csv('./redo/csv_files/Lending-company.csv', index_col = 'StringID')
sales_products = data.copy()

print(sales_products.Product.head())
print(sales_products['Product'].head())

#we can also combine different columns to print its output as head or tails

#if we want to get a dataframe of a single column we have to use double bracket
#this will return a nested list containing a single element
#when we want to return multiple columns we have to set it as a list with double brackets to get an appropriate return

print(sales_products[['Location', 'Product']].head())

