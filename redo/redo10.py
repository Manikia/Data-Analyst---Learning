import pandas as pd
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


#string accessors
operational_kpi = pd.Series(['employee satisfaction rating', 'employee churn rate'])
#we cannot use the typical strip insrtead we have to use the indexing to let it know which one we want to remove it from
removedE = operational_kpi[0].lstrip('employee')
removedE2 = operational_kpi[1].lstrip('employee')
print(removedE)
print(removedE2)

#we can also store both of the strips in a series by doing the below:
seriesOutput = pd.Series([operational_kpi[0].lstrip('employee'), operational_kpi[1].lstrip('employee')])
print(seriesOutput)

#string accessor looks into the object attributes, it can access the values of the series as strings instead
operational_kpi.str #wont give us a valuable output so we have toi do the below
print(operational_kpi.str[1]) #this will only return the character at position 1 not the value

#using str we can strip and it will be able to remove everything in the series without ahviung to create multiple codes of line
stripwStr = operational_kpi.str.lstrip('employee')
print(stripwStr)

#if not all values are string and we have a string and an int, try to remove a string we will get  NaN object output 

#if we want to see if the object in our series contain a specific object we can use contain to make sure every index has what we are looking for, it will return which are true and the ones with false dont have what we are looking for included:

house_prices = pd.Series(['$400,000', '$500,000', '$600,000'])
print(house_prices.str.contains('$'))

#to preprocess text data we can do the below:
time_horizon = 1,3,12 #tuple
products = ['Product A', 'Product B']

#the .format method is only applicable in string values
#the format can use multiple inserts when outputting and uses the curly braces in the string as placeholders for the format
#we can also use the brackets in the string to be implicit or explicit in our positions, for example originalls when we dont add anything to the brackets its first 0 then 1 but if we switch it it will switch the way its outputted by doing prodyuct first instead of time first
print('Expected sales for a period of {0} months for {1}:'.format(time_horizon[0], products[1]))
#we can also use keywords instead of values
print('Expected sales for a period of {t_hor[1]} months for {prod[1]}:'.format(t_hor = time_horizon, prod = products))
print('Expected sales for a period of {t_hor[1]} months for {prod[1]}: ${sales}'.format(t_hor = time_horizon, prod = products, sales = 10000))

