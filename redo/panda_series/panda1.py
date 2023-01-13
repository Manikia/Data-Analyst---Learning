import pandas as pd

data = pd.read_csv('./redo/csv_files/Location.csv', squeeze = True) #reformatting the series 
location_data = data.copy() #we are copying the data to new variable location_data

#we can then look at the data that we have by using describe:
print(location_data.describe())

#there are two different unique methods we can use to look at our data
#.nunique() will return the amount of unique data we have while
#.unique() will return what unique data we have

