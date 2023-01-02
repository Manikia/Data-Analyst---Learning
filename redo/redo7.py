#exporting xlsx/excel files to python
import pandas as pd

filename = './redo/csv_files/Lending-company.xlsx'
my_xlsx_data = pd.read_excel(filename, index_col = 'LoanID') #this will remove the indexing and set the index to be the loanid
print(my_xlsx_data)

filename2 = './redo/csv_files/Lending-company.csv'
format_output = pd.read_csv(filename2, usecols = ['StringID', 'Product', 'TotalPrice'], index_col = 'StringID')
print(format_output.head())

#for the above, the column and the index must be present to print it, so if we have stringID only in index_col and not in usecols, it wont output and return an error, we have to have it in both areas

filename3= './redo/csv_files/Lending-company-single-column-data.csv'
csv_data_2 = pd.read_csv(filename3, delimiter = '\,', engine = 'python') #we add the slash ebcause we are working with a raw string
#we will get an error that the python engine is falling back so we will have to add engine = 'python' at the end to prevent it from failing
print(csv_data_2)
#also instead of delimiter we can use sep/delimiter

#on another lesson we are going to learn how to remove the quotation when outputing

singleCol = './redo/csv_files/Customer-Gender.csv'
df_single_col = pd.read_csv(singleCol)
print(df_single_col)

#if we want to remove single dimension entries from the shape of an array we do the squeeze method
#we use squeeze to call a series 