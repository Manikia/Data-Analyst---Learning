import pandas as pd

data = pd.read_csv('Location.csv', squeeze = True)
location_data = data.copy()

location_data.sort_values(ascending=False)

location_data_sv = location_data.sort_values(ascending=False)

print(location_data_sv.sort_values()) #this sorts the values of the output, this is only useful if we want ton obtain the sorted index structure as a separate entitiy for some reason
print(location_data_sv.sort_index())#this sorts the index values but it doesnt overwrite the contents

#if we want to organize both we have to do as below
location_data_sv = location_data_sv.sort_index(ascending = True) #we do this because we are telling it that we want to organize the index and since we set ascedning as true it will ascend them both
print(location_data_sv.head())