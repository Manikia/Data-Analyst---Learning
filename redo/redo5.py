#files: python only maintains two categories of files, text and binary
# text files are also known as flat files or ascii files
#structured data is like an excel file, semi structured is like emails because it still have specified tags but its a little unstructured and then instructured data is no torganized and its like having a foledr with audio files or images: all of these combined is what is called big data

#plain files: each data is tored as a separate line so we dont need separators
#flat files: each data value is separated by a separator

#different type of separators: comma-separated value which is separated by a comma, character-separated value which is separated by a comma, semicolon or tab, a delimiter-separated valyue which destincts a row or rows in a table, or a tab-separated value which is a type of dsv and its formatted as a table when in the text file 

#relational database: contains multiple data tables that relate to each other in a certain way 
#flat file database: a flat file corresponds to a single table from the relational database, it denotes a relational database composed of a single data table

filename = 'source.txt'
file = open(filename, mode = 'r')
#print(file.read()) #we do this if we want to format to read the details in the text but it will only print once, it wont print again. to avoid this we have to initialize the read to another variable. also but if we do just print(file) then it will return a wrapper
fileText = file.read()
print(fileText)
print(fileText)

#then we close the file bc if we dont we can lose control of the files status and we might get hacked
print(file.closed) #will return if its closed
file.close()
print(file.closed)
