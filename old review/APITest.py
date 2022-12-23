import requests
import json
import numpy as np
import pandas as pd

base_site = "http://192.168.0.136:3030/temperatures/formatted-history"
param_url= base_site + '?HomeHumidity=39'
print(param_url)
response1 = requests.get(base_site)

data = json.dumps(response1.json(), indent = 4)
data1 = response1.json()
data2 = data1['history']

print(data['HomeHumidity'])



