#list comprehensions:creating lists from existing lists but in an elegant way

numbers = [1,13,4,5,63,100]

#getting squared of all int in the list
new_numbers = []

for n in numbers:
    new_numbers = n*2
    print(new_numbers)

print(type(new_numbers))

#instead of doing the above we can create an output expression for an element in iterable

new_numbers = [n*2 for n in numbers]
print(new_numbers)
print(type(new_numbers))

#we can also convert this to a simple way:

for i in range(2):
    for j in range(5):
        print(i+j, end = ' ')

output = [i+j for i in range(2) for j in range(5)]
print(output)

print(type(output))

#we can also output then as a list by adding brackets
output = [[i+j for i in range(2)] for j in range(5)]
print(output)

#tasK deliver a list containing integers equal to the values of the generated sequence raised to the power of 3 on the condition that the values are odd numbers
print([n**3 if n %2 != 0 else "even" for n in range(1,11)])
#if we want to create an else statement the if statement needs to be in the middle or it wont work

#when iterating we can add what we want to filter out on the right side of the function from the iteration
for i in range(2):
    for j in range(5):  #nested in this situation will have j printed as many times as i is presented
        print([i,j])

print([[i,j] for i in range(2) for j in range(5)])




