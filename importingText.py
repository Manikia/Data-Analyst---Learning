import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col = 'LoanID')
lending_co_data = data.copy() #creating file object

#if we want to look at information in the last column we have to do -1 to show we want the last one
lending_co_data.iloc[:, -1]

#we can also do as below where it only gets the row specifier
lending_co_data['TotalPrice'].iloc[0] #for example this will return only the total price in the position of 0

#if we dont use iloc then we have to use the exact id number in the brackets where iloc is and remove iloc to get the same result, if not it wont work, shown as below should work:

lending_co_data['TotalPrice'][1]

#using iloc we can use strings of the name of what indexes we are looking for or index numbers, its vise versa and can work together

#chained indexing is when The flexibility of pandas allows for chained indexing, where you can repeatedly index the outcome of a previous indexing operation but its not encouraged to use

#we can also use both in one line
print(lending_co_data.loc[:, 'TotalPrice'].iloc[[0,5]])