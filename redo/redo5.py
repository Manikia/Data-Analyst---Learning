#files: python only maintains two categories of files, text and binary
# text files are also known as flat files or ascii files
#structured data is like an excel file, semi structured is like emails because it still have specified tags but its a little unstructured and then instructured data is no torganized and its like having a foledr with audio files or images: all of these combined is what is called big data

#plain files: each data is tored as a separate line so we dont need separators
#flat files: each data value is separated by a separator

#different type of separators: comma-separated value which is separated by a comma, character-separated value which is separated by a comma, semicolon or tab, a delimiter-separated valyue which destincts a row or rows in a table, or a tab-separated value which is a type of dsv and its formatted as a table when in the text file 

#relational database: contains multiple data tables that relate to each other in a certain way 
#flat file database: a flat file corresponds to a single table from the relational database, it denotes a relational database composed of a single data table

# fixed width datafiles are when a file and its columns have a set width so add informastion and cant be more or less than what intended/set

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
    
