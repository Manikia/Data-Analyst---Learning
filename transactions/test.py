# import pandas as pd

# t = pd.read_csv('data.csv').to_string()
# for i in range(1): #these are are rows
#     for j in range(end = ' '): #and these are our columns
#         #when nesting this will print as many times as the above loop tells it to
#         print([i,j])

from csv import reader
# open file in read mode
with open('data.csv', 'r') as read_obj:
    monikaBalance = 0
    mannyBalance = 0
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        #index.setdefault(row[0], [])
        if(row[2] == 'MONIKA G ANGEL'):
            monikaBalance += float(row[4])
        else:
            mannyBalance += float(row[4])
    
    print("Bobby has a balance of: " + str(monikaBalance))
    print("Manny has a balance of: ", mannyBalance)