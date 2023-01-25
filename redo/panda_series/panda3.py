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

#iloc ( integer location) is an attribute indexer or accessor
#the same rules fall into iloc as it falls under indexing which is only for python lists, pandas series by index posision and its only integert based or position based indexing
data2 = pd.read_csv('./redo/csv_files/Lending-company.csv')
lending_co = data2.copy()

#print(lending_co[0]) #we cant do this to look at the first location of our index instead we have to use .Product or ['Product'] as shown before
#but if we want to use the integer to find the index we have to use iloc
print('location information\n')
print(lending_co.iloc[1])
#as we can see we get an output of the second row which is loanID 2 and if we want to see more details about it we can specify the row and the column instead to get a specific data
#when using iloc to find a numerical position we dont count the index when counting
print(lending_co.iloc[1,3]) #in this case its the first row and the 3rd column we want to look at but as we remember indexes start at 0 so we have to add one more position to the right side/column
print('another\n')
print(lending_co.iloc[1,:]) #the second row and all the columns
print(lending_co.iloc[:,4]) #all the rows which will always be the first column +1 but only the 5th column
print(lending_co.iloc[0:3]) #we can also create a start and stop and skip like in range to get a specific part of the table and in this case we want all the rows and to stop on the third position (or 2nd if we are indexing by 0)

print(lending_co.iloc[:,0:2])# we can also do a situation where we want a specific amount of columns instead but all the rows if we do this

#we can also get a subset of the table by doing a matrix style and whatever overlaps in columnxrow it will return:
print(lending_co.iloc[2:6,2:5])  #basically[3,5][3,4]

#something to keep in mind is that if we define the index or we leave the index as is, it will always show on our output table

print(lending_co.iloc[6, 7:13]) #if we do a single row we have to do a number before to get our number, its weird because when we do #:# it always does the number we are on for the right side of the colon but not in these cases


print(lending_co.iloc[[1,4], :]) #if we want different rows that arent nexct to eah other we do it this way but what is weird about this

print(lending_co.iloc[:, [1,4]])

#using .loc

data3 = pd.read_csv('./redo/csv_files/Lending-company.csv', index_col = 'StringID') #im telling this that I want the index to be stringID not the default index so it will take priority when going through the table
lending_co_data = data3.copy()

#we can use loc to get the row of a table, multiple rows as well

print(lending_co_data.loc['LoanID_3'])
print(lending_co_data.loc['LoanID_3', :])

print(lending_co_data.loc['LoanID_3', 'Region'])#this is basically what iloc is but instead of it being all numerical we can all the table names by its name

#this location_co_data['Location'] is the same as location_co_data[:.'Location']


data4 = pd.read_csv('./redo/csv_files/Lending-company.csv', index_col = 'LoanID')

lending_c02 = data4.copy()

print(lending_c02.shape)
print(lending_c02.iloc[:,-1]) #if we want to get the last column we have to do -1

#we can use iloc or loc for a series reference but it has to be one number it cant be a row and column like we usually do, only row specifier since we are already spoecifycing the column in totalprice
print(lending_c02['TotalPrice'].iloc[0])
#the above is basically saying lets look at the column for totalprice and go to the first position of its data which will be 17600

#we can also add only the digit as a bracket but it has to match the index number ex:
print(lending_c02['TotalPrice'][1]) #1 since the loanid starts w loanid = 1

data5 = pd.read_csv('./redo/csv_files/Lending-company.csv', index_col = 'StringID')
lending_co3 = data5.copy()

#we can also use the name of both column and row to get our output 
print(lending_co3['TotalPrice']['LoanID_1'])

#we can also add multiple by doing the below:
print(lending_co3.loc[['LoanID_1','LoanID_6'], :])
#with the above we get two different rows with all the columns 
print(lending_co3.loc[['LoanID_1','LoanID_6'], ['Product']])

#we can also call it as a dataframe by doing:
print(lending_co3.TotalPrice['LoanID_1'])

#the only time we can combine iloc and loc is if we want to refer to the position of certain wvalues in the DF column
print(lending_co3.loc[:, 'TotalPrice'].iloc[[0,5]])
#in this case we are saying we want to look at all the columns with total price but we are limiting our search to only show the first and 6th row

