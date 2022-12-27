#importing json files

import json
import pandas as pd

json_file = './redo/csv_files/Lending-company.json'
#json_test = json.loads(file_name) #we use this to convert a string to a dictionary
json_test = pd.read_json(json_file) #we use this to read the ocntext files of a json file and stores as a dataframe directly
print(json_test)