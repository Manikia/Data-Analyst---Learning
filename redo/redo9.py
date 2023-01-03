#exporting data from python object to a text file
import pandas as pd
import numpy as np
#we can export data that we have from different files to different file formats by doing the below:

filename = './redo/csv_files/Lending-company.csv'

data = pd.read_csv(filename)

toCSV = data.to_csv('./redo/exportedFiles/converted_to_csv.csv') #we create the file inside the paraenthesis  
toJSON = data.to_json('./redo/exportedFiles/converted_to_json.json')
toEXCEL = data.to_excel('./redo/exportedFiles/converted_to_excel.xlsx') #doing it this way will export the file with an index, if we dont want an index when exporting we have to add index=False
toEXCEL = data.to_excel('./redo/exportedFiles/converted_to_excel_no_index.xlsx', index = False)

#using np.save will save the file to a npy file type
lending_co = np.genfromtxt('./redo/csv_files/Lending-Company-Saving.csv', delimiter = ',', dtype = str)

#using the save we have yo set it as np.save('file-name', dataset_variable)
numpySave = np.save('./redo/csv_files/Lending-Company-Saving', lending_co) #telling it that we want to save it sa npy in the new name (L) from the information on the right

#using the npy file conversion is better when using npy files since it loads it .13 seconds but its a bit slower with csv and txt in order
#using the np.load will make sure that the data we return in our file is returned in its original form, because if we were to import, it takes the edited form not the original

original_data = np.load('./redo/csv_files/Lending-Company-Saving.npy')
print(original_data)


#np.savez is another method where we can save data as a npz file
#this type of file is a zipper archieved file names after the variables they contain

numpySavez = np.save('./redo/csv_files/Lending-Company-Saving', lending_co)


