#working with text data
#to print in python we use the same way we do in C with %s and instead of a comma when adding the variable we do %
#like thid: print("blah blah "%s"" % product_category")
#to add a float we do $%.(decimal places)F

#if we want to output multiple variables it gets a little weird and we have to do the below:
quantities = [500, 600]
product_category = ['A', 'B']
test = [1,2]
i = 1
print("Currently, we have %d units of category \"%s\" products in store. and this number %s" % (quantities[i], product_category[i], test[i]))
#we add the backslashes that we have in the string becuase we want it to print with the quotations

#manipulating python strings
#\t : tab \r :replaces the beginning to the right side of \r by taking the amount of characters it needs

#we can replace parts of a string using replace()
s = 'Price per unit'

s1=s.replace('Price', 'Cost')
print(s1)

#we can check if something ends or starts with a specific string by doing: something to keep in mind is that it doesnt have to be a complete sentence it can just be a part of it and itll work

print(s1.startswith('Cost')) #returns true or false
print(s1.endswith('nit'))


#using split will return the string turned into a list of separate values
print(s1.split(' '))

print(s1.split('per'))

#we can also indetify the maximum number of splits able to be done in the execution (we can also remove maxsplit and just add the number and itll work the same way)
print(s1.split(' ', maxsplit= 1))

s2 = 'Mr., John, Wilson'
print(s2.split(','))
print(s2.split(',')[0]) #since we split it with the comma, we can all each array index by doing the brackets

#uppercase we do .upper()
#lowercase we do .lower()
#capitalize the first letter .capitalize()
#uppercase every start of a string .title()


#using strip will remove everything in the beginning or end based on how it matches with waht i have inside the strip
#it only removes the beginning or end that matches whats inside, we can add whatever and as long as its present in the beginning or end itll remove
s3 = '    quarterly earnings report    '
print(s3.strip(' qt'))

#we can also specify to only remove the left or right side of the string we have .lstrip() or .rstrip()
print(s3.lstrip(' '))

#if we want to remove a word fromt the string we have to do it one at a time so we would remove the spaces and then the word after so that it can work or else it can remove parts of the other words we have in the sentence
s4=s3.strip(' ')
print(s4)
print(s4.lstrip('quarterly'))
print(s4.rstrip('report'))



