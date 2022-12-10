#this file is so that I can have a refresher of what I learned but forgot about python

#we cant print out an int and a string together so we cascade by using str() to print it together
y = 10
print(str(y) + " dollars")

#we can do to the power by doing **
x = 5 **3

#todo an if operation we set as
if 5 ==15/3:
    print('yes')

#to do an if else operation we do
if x>3:
    print('case1')
else:
    print('case 2')

#we can use elif if we want to do else if
if x>3:
    print('if')
elif x < 3:
    print('elif')
else:
    print('else')


#creating a function
def simple():
    print('sentence')
simple() #must call after initializing the function
#function with a parameter:
#def function_name (parameters):
    #fucntion body
def plus_ten(a):
    return a + 10 #body of function
print(plus_ten(2)) #when we initialize we set the number so that it can pass as a in the function
#the 2 above where the position is is called an argument


#we can use a function inside another function
def wage(w_hours):
    return w_hours * 25

def wageBonus(w_hours): 
    return wage(w_hours) + 50

print(wage(8))
print(wageBonus(8))

#if save 100 then +10 else +0

def allowance(save):
    if save >= 100:
        return print("Allowance icnreased: " + str(save + 10))
    else:
        return print("Allowance stayed same: "  + str(save))

allowance(99)

#we can do multiple values by doing
def subtract(a,b,c):
        result = a-b*c
        return result
print(subtract(10,3,2))

#we can use the below
#type() to know what type
# int() to cascade to int
# float() to cascade to float
# str() to cascade as String
# max() to find the max in a sequence
# min() to find the min in a sequence
# abs() returns absolute value removes the negative sign and makes them positive
# sum() calculates the sum of all elements in a list set as an argument
# round() rounds to nearest 
# to do the power we do ** or pow(x,y) where X is the base and Y is the multiple
# len() finds the length of an object like how many chars in a word/array length

# to create a list we have to use brackets and single quotation
participants = ['John', 'leila', 'Gregory', 'Cate']
print(participants[1])

# to get the last element we do
# and if we want to get the second last we do -2 and so on
print(participants[-1])

#to switch positions we do:
participants[-1] = 'Maria'
print(participants)

# we can remove an object from a list by using del
del participants[2]
print(participants)

# to add to the list we do <object name>.append()
participants.append('Dawayne')
print(participants)

# to add multiple thigns to an object we do .extend() if we were to do append it will add the new list as an array inside an array
participants.extend(['George', 'Catherine'])
print(participants)

# to get a specfic area of an arrays length we have to use colon. For example x:y where x is the beginning and y is the end +1
print(participants[1:3]) #this will return leila and maria

#to get the first two you do
print(participants[:2])

#to get the last 2 we do
print(participants[-2:]) # from right to left
#or
print(participants[4:]) # from left to right

# if we want to find the position of something we do .index() and it will show us the index position
print(participants.index('Maria'))

#to add to the list we do:
Newcomers = ['Joshua', 'Brittany']
bigger_list = [participants, Newcomers]
print(bigger_list)

# we can sort the information inside the object by using sort()
participants.sort()
print(participants)

# we can reverse the order by adding reverse = True inside the parenthesis
participants.sort(reverse = True)
print(participants)

# tuples are defined as parethesis and cant be changed: y = (40,21,42)

# to separate things we use .split()
(age, school_years) = "30,17".split(',')
print(age)
print(school_years)

#dictionaries we can sort by having a key and an object: key value pairs
# the key or the value can either be single or double quotes
dict = {'k1': "cat", 'k2': "dog", 'k3': "mouse", 'k4': "fish"}
print(dict) #prints values from key

# to add a key value we do: and we can use this structure to replace as well
dict['k5'] = 'parrot'
print(dict)
dict['k4'] = 'betta'
print(dict)

# we can set multiple values in one key as well:
dep_worker= {'dep1': 'Peter', 'dep2':['jennifer', "Michael", 'Tommy']}
print(dep_worker['dep2'])

# we can also create an emty dictionary and populate:
team = {}
team['Point Guard'] = 'Dirk'
team['Goalie'] = 'Derick'
# and so on

# we can use .get() to return us the value from a key as well
print(team.get('Point Guard'))

#for loop we do:
even = [0,2,4,6,8,10,12,14,16,18,20]
for n in even:
    print(n, end = ' ') #prints every index in the array
    #the space above is to make it all print in one line
print('\n')
x = 0
while x<= 20:
    print(x, end = ' ')
    x = x + 2 # or x += 2 

# to create a patten range we can use rage
# range(start = first number on list, stop = last value + 1, step = distance of two consecutive values)
# if we dont indicate anything on step then it will step as 1
print('\n')
print(range(10)) #this will print the range but not the list
#to print the list we do the below
print(list(range(0,10)))

print(list(range(4, 10))) #this will range starting from 4 and ending at 9

#if we want to specify by what step we want it to read we do
print(list(range(0, 20, 2))) # since I did every second it will do every even until 19
print('\n')
# try outs
for n in range(10):
    print(2**n, end = ' ')
print('\n')

for x in range(20):
    if x%2 == 0:
        print(x, end = ' ')
    else:
        print('Odd', end = ' ')

def count (numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total = total + 1
    return total
list1 = [1,14,234,23,23445,65,34,7]

print('\nthese amount of numbers are less than 20: ' + str(count(list1)))

prices = {'box of spaghett':4, 'lasagna': 5, 'hamburger': 2}
quantity = {'box of spaghett':6, 'lasagna': 10, 'hamburger': 0}

total = 0
for n in prices:
    total = total + (prices[n] * quantity[n])
print(total)

#if we want to use all arguments in a function we do:
def goals(*a):
    return sum(a)

# when we get a user input we use this:
name = input('Whats your name?: ')
#and to use it we have to add the f infront to show that its a function and use braces
print(f'the name is {name}')

#objects are like strings, floats, int 

#functions have many parameters while methods have one objects as its parameter
#function() and object.method()
# we can import modules which are like packages
#there are 4 ways to import a module:
# import math
# math.sqrt(2)

# from math import sqrt
# sqrt(2)

# from math import sqrt as s
# s(36)

# import math as m #this is looked down though
# m.sqrt(2)

# from math import * #this gets all files
# sqrt(2)

#using <something>.upper() makes it uppercase

#to repeat a string we can use a multiply operator

