#data frames topic
#series are single (1d) column data where it represents a single variable while dataframes are multi column (2d) data and have different variables and each column can contain its own type

#series is a single point reference since its only one column but a dataframe is a double point reference since it needs an x and y to find the exact location

#creating dataframes

import pandas as pd #dataframes come from pandas
#data1 = {'COLUMN':['ROW1', 'ROW2', ...], 'COLUMN2':[ROW1, ROW2, ...]}
data1 = {'ProductName':['Product A', 'Product B', 'Product C'], 'ProductPrice':[22250, 16600, 12500]}
df1 = pd.DataFrame(data1)
print(df1)

#we can initialize the index by:
index = ['A','B','C']
df1 = pd.DataFrame(data1, index)
print(df1)

#we can also initialize a dataframe as:
data2 = [{'ProductName':'Product A', 'ProductPrice': 22250}, {'ProductName':'Product B', 'ProductPrice': 16600}, {'ProductName':'Product C', 'ProductPrice': 12500}]
df2 = pd.DataFrame(data2)
print(df2)

#we can also create multiple prices for one product by doing:but it will ruin our structure since everything else is only one price 
data2 = [{'ProductName':'Product A', 'ProductPrice': 22250}, {'ProductName':'Product B', 'ProductPrice': 16600}, {'ProductName':'Product C', 'ProductPrice': [12500, 100000]}]
df2 = pd.DataFrame(data2)
print(df2)

# we are going to define by setting a series and using the variables to initialize isntead of writing them
ser_products = pd.Series(['Product A', 'Product B', 'Product C'])
ser_prices = pd.Series([22250, 16600, 12500])
print('\n')
data = {'Product Name':ser_products, 'Product Prices': ser_prices} #im initializing a series with two columns where its the name and prices and I will call it by doig the dataframe
print(data)
print('\nvs\n')
data = pd.DataFrame(data)
print(data)
#from what i see, when we dont do dataframe it wont format it correctly and it wont structure it as a table

#we can initialize the index as well
ser_products2 = pd.Series(['Product A', 'Product B', 'Product C'], index = ['A', 'B', 'C'])
ser_prices2 = pd.Series([22250, 16600, 12500], index = ['A','C','B']) #im testing if when we initialize these our of order they would match the previous initialization
data2 = {'Product Name':ser_products2, 'Product Prices': ser_prices2}
data2 = pd.DataFrame(data2)
print(data2)

#from what i tested if we initialize the index of the first series it will be like the master one and the rest will try to match based on how the master was set and in this case I switched the order of the second series and they matched their indexes in the output


#we can also create a dataframe by using multiple lists
data3 = [['Product A', 22250], ['Product B', 16600], ['Product C', 12500]]
data3 = pd.DataFrame(data3)
print(data3)
#now we can initizlise the column names like
data3.columns = ['Product Names', 'Product Prices']
print(data3)
# we can initialize the index names as
data3.index = ['A','B','C']
print(data3)

#professionally creating a dataframe
data4 = pd.DataFrame(data=[['Product A', 22250], ['Product B', 16600], ['Product C', 12500]], 
                    columns = ['Product Names', 'Product Prices'], 
                    index = ['A','B','C']) 
print(data4.shape)#this will give us the dimension of the dataframe


