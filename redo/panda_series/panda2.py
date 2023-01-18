#dataframe review
import pandas as pd
import numpy as np

array_a = np.array([[3,2,1],[6,3,2]])
array_b = [[1,2,3],[2,4,5]] #even thouhg it looks like we are creating an array we are creating a list, if we want to create an array we have to use dataframeas
print(type(array_a))
print(type(array_b))

print(pd.DataFrame(array_a)) #this creates a 2d table of the details on the array we created throuhg the dataframe
df = pd.DataFrame(array_a, columns = ['Column1', 'Column2', 'Column3'], index= ['Row1','Row2'])

print(pd.DataFrame(df))

data = pd.read_csv('./redo/csv_files/Lending-company.csv', index_col = 'LoanID')
print(data.head())





