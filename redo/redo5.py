#files: python only maintains two categories of files, text and binary
# text files are also known as flat files or ascii files
#structured data is like an excel file, semi structured is like emails because it still have specified tags but its a little unstructured and then instructured data is no torganized and its like having a foledr with audio files or images: all of these combined is what is called big data

#plain files: each data is tored as a separate line so we dont need separators
#flat files: each data value is separated by a separator

#different type of separators: comma-separated value which is separated by a comma, character-separated value which is separated by a comma, semicolon or tab, a delimiter-separated valyue which destincts a row or rows in a table, or a tab-separated value which is a type of dsv and its formatted as a table when in the text file 

#relational database: contains multiple data tables that relate to each other in a certain way 
#flat file database: a flat file corresponds to a single table from the relational database, it denotes a relational database composed of a single data table

# fixed width datafiles are when a file and its columns have a set width so add informastion and cant be more or less than what intended/set
import pandas as pd
import numpy as np

filename = './redo/source.txt'
file = open(filename, mode = 'r')
#print(file.read()) #we do this if we want to format to read the details in the text but it will only print once, it wont print again. to avoid this we have to initialize the read to another variable. also but if we do just print(file) then it will return a wrapper
fileText = file.read()
print(fileText)
print(fileText)

#then we close the file bc if we dont we can lose control of the files status and we might get hacked
print(file.closed) #will return if its closed
file.close()
print(file.closed)

#character meaning when opening a file: r:reading, w:writing, x:create a new file and open for writing, a:open for writing and append to the end of file if exists, t:text mode

#its better to use a with method when opening a file, so instead of doing what we did above we can cut it down adn do this: but as before we have to set it to another variable or it wont print

#with statement is better because it closes the file but the other method doesnt close it and we might miss closing it

with open(filename, mode = "r") as output:
    out_put = output.read()
    print(out_put)
    print(out_put)

with open(filename, "w") as writing:
    writing.write("Adding new information")
    
with open(filename, mode = "r") as newoutput:
    new_out_put = newoutput.read()
    print(new_out_put)
    print(new_out_put)
    

#importing csv files it will return everything jumbled up
filename2 = './redo/csv_files/Lending-company.csv'
file2 = open(filename2, mode = 'r')
text2 = file2.read()
print(text2)

#if we want to organize the output we can do thebelow:
print(pd.read_csv('./redo/csv_files/Lending-company.csv', header = 0))
#by using header we can change the start of the information on the #nth digit

#if we dont want to use the default index value to number our output we can use index_col to move our indexes to the other column
print(pd.read_csv('./redo/csv_files/Lending-company.csv', header = 0, index_col = 0))

#if we want to name our column we use name = [] and add the new column name, we dont use columns as we thought we would

#two ways to import data with numpy: np.loadtxt() and np.genfromtxt()
#np.loadtxt() is data is ready to be imported and used and its faster
#np.genfromtxt() indicated that the finction created the dataset from text file and is more flexible

lending1 = './redo/csv_files/Lending-Company-Numeric-Data.csv'
lending_co_1 = np.loadtxt(lending1, delimiter = ',') #delimiter means there is a separation
print(lending_co_1)

#we use the two text outputs shown to show us what is inside the text file and although both outputs are exact, if we use the np.array_equal(file1, file2) it will show us if its equal and although they output the same thing, if we input a NaN csv information to the loadtxt it will break but loads faster if we input a correct information while the genfromtxt will work but will take a longer time to process

#using dtype will reformat everything as the type we are initializing as and if we use loadtxt it can work since its looking for a type but cant find it so we are setting everything even the empty cells as a type which will work when working with loadtxt
loadtxt = np.loadtxt('./redo/csv_files/Lending-Company-Numeric-Data-NAN.csv', delimiter = ',', dtype = str)
print(loadtxt)

#if we want to skip some of the beginnig row of data we can use skip_header = # to let us know how many we want to skip, we can do the same with skip_footer to do the bottom rows

#we can do the same from below but with columns instead as usecols = # which means we are telling it which ones we want to see

# we can use what we have covered to set the different outputs to different variables if needed
lending_5, lending_0, lending_1 = np.genfromtxt('./redo/csv_files/Lending-Company-Numeric-Data-NAN.csv', delimiter = ',', usecols = (5,0,1), skip_header = 2, skip_footer = 2, unpack = True) #this will set 3 different variables to each of the different edits which are the different columns and skipping the header and footer, if we were to continue this without the unpack it will return an error since its a lot of variables but to permit it we do unpack = true

print(lending_5)
print(lending_0)
print(lending_1)

