#squeeze method

import pandas as pd
import numpy as np

#squeeze method can only work for one dimensional sequences
#converts a column DataFrame to a series
#we can use 0 or rows to squeeze the data in a vertical axis
#we can yse 1 or columns to squeeze the data in horizontal axis
filename = './redo/csv_files/Lending-company.csv'
data1 = pd.read_csv(filename, usecols = ['Product'])
squeeze1 = data1.squeeze(1)
print(squeeze1)

filename2 = './redo/csv_files/Customer-Gender.csv'
data2 = pd.read_csv(filename2)
squeeze2 = data2.squeeze(1)
print(squeeze2)

filename3 = './redo/csv_files/Customer-Gender.csv'
data3= pd.read_csv(filename3)
squeeze3 = data3.squeeze(0)
print(squeeze3)




