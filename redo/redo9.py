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
#print(original_data)


#np.savez is another method where we can save data as a npz file
#this type of file is a zipper archieved file names after the variables they contain
#what savez can do is save multiple datasets in one npz file and we can just call it with its array position and we can also name them which will be shown

# lending_co = np.genfromtxt('./redo/csv_files/Lending-Company-Saving.csv', delimiter = ',', dtype = str)

# original_data = np.load('./redo/csv_files/Lending-Company-Saving.npy')


numpySavez = np.savez('./redo/csv_files/Lending-Company-Savez', lending_co, original_data)
lending_data_savez = np.load('./redo/csv_files/Lending-Company-Savez.npz')
print(lending_data_savez["arr_1"])  #calling lengins_co information since we did arr_0 but we can rename thse as well
#print("haryNuts")

#we can rename the array by doing:
numpySavez = np.savez('./redo/csv_files/Lending-Company-Savez', lending = lending_co, original = original_data)
lending_data2 = np.load('./redo/csv_files/Lending-Company-Savez.npz')
#to check the different files in the npz we do:
print(lending_data2.files)
print('\nprinting original data\n') 
print(lending_data2["original"]) 

#learning about np.savetxt() which we will save data in text files/format
#np.savetxt is able to save datasets to text files like .txt or .csv format
np.savetxt('./redo/csv_files/Lending-Company-Savez.txt', lending_co,  fmt = '%s', delimiter = ',') #when using savetxt we have to add more parameters, we have to add: if its txt or csv, the format of the data which will always be after the file, formatting the data will let the compute know what kind of data it will be working with and how to format it appropriatly, 
#format can include: c:character, d or i: signed decimal integer, e or E: scientific notation, f:decimal point, o:signed octal, u:unsigned decimal, s:string of characters, x,X:unsigned hexadecimal integer
#when we use savetxt we have to import the file instead of loading which means we have to use genfromtxt to output it
lending_save_txt = np.genfromtxt('./redo/csv_files/Lending-Company-Savez.txt', delimiter = ',', dtype = str)

print(lending_save_txt)

#its better to use savetxt because it can be opened in a variety of text editoprs rather than savez where its strict where it can be opened from

