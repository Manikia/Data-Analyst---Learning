#importing json files

import json
import pandas as pd

prices_per_product = '{"Product A": 22250, "Product B": 16600, "Product C":12500}' #if we define a string and its values like this we can convert it later as a dictionary
print(type(prices_per_product))
json_product_convert = json.loads(prices_per_product) #we use this to convert a string to a dictionary
print(type(json_product_convert))


json_file = './redo/csv_files/Lending-company.json'
json_test = pd.read_json(json_file) #gets the data and stores it as a dataframe directly with tables and such
#we can also define a variable to the dataframe we converted so that we can reuse it and not alter the original information
new_csv_data = json_test
print(new_csv_data)

# json_file = './redo/csv_files/Lending-company.json'
# #json_test = json.loads(json_file) #we use this to convert a string to a dictionary
# #json_test = pd.read_json(json_file) #we use this to read the ocntext files of a json file and stores as a dataframe directly
# print(json_test)

