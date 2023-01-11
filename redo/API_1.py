#intro to api requests
#GET: obtains data from a server and parameteres adre added in the url also the data is public so it sint used for sensitive data
#POST: alter state or send confidential into, the parameters are added in a sepaate body. ex: logging into an account w user and pw those are post requests
#request codes: 200 ok and 404 error

#course forces to sign up so im not going to and will use a jsonplaceholder instead
import requests
import json
import pandas as pd
base_url = 'https://jsonplaceholder.typicode.com/posts' #we are initializing a variable to the page that we want to pull/get a request from

jsonGet = requests.get(base_url)
#to check if the process went through we do: request.ok or jsonGet.status_code
#to get a body response of its data we do: and if we want to return in byte format we do the same but instead w .content
print(jsonGet.text)
print(jsonGet.json())

#we can fix the readability more by importing json and doing the below
#loads(string): converts a json formatted string to a python object
#dumps(object): converts a object back to a string with options to make the string prettier
    #parameters are able to pass situations where the type does not match or maybe an error might pop up so we add the parameter, there is also a separator is set as: should be an (item_separator, key_separator) tuple. The default is (', ', ': ') if *indent* is None and (',', ': ') otherwise. To get the most compact JSON representation, you should specify (',', ':') to eliminate whitespace.
#dumps info: https://pynative.com/python-json-dumps-and-dump-for-json-encoding/

convertedJson = pd.read_csv('./redo/csv_files/creditWells.csv')
convertedJson.to_json('./redo/exportedFiles/bankAPIrequest.json')

print(json.dumps(jsonGet.json(), indent = 4))

print(jsonGet.json().keys())


