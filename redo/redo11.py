#iterations

t = (4,5,6,7) #tuple
l = [10.5, 20.75, 30.00] #list

s = 'abcde'

for i in range(len(t)):
    print(t[i], end = '') 
print('\n')
for i in t:
    print(i, end = '') #we are printing everything from t and we dont have to do t[i] because this is an enhavned for loop
#in the above example the t is an iterable which means we can iterate through it
print('\n')
for i in s:
    print(i, end = '') #we can also go through every string 
print('\n')


#nested for loops

for i in range(2):
    for j in range(5):  #nested in this situation will have j printed as many times as i is presented
        print(j)

for i in ['Product A', 'Product B']:
    for j in range(5):  #nested in this situation will have j printed as many times as i is presented
        print([i, j])

#we dont ahve to iterate in loops over numbers we can use strings as well

products = ['Product A', 'Product B']
exp_sales = [10000, 11000, 12000, 130000, 14000]

for i in products:
    for j in exp_sales:
        print([i, j])


#triple nested for loops
time_horizon = (1,3,12)

for i in products: #2
    for j in exp_sales: #5
        for k in time_horizon: #3  #this will print 3 times the previous so it will be k for every j so 15 since we are printing the three time horizon for all the sales
            print([i, j*k])
            
#its good habit to change the i names as its relation in the loop like so:

for prod in products: 
    for sales in exp_sales: 
        for t_hor in time_horizon:
            print('Expected sales for a period of {0} months for {1}:${sales}'.format(t_hor, prod, sales = sales*t_hor))
            
#in some situations we can sqitch the placement of the loops and it will output differently
for prod in products: 
    for t_hor in time_horizon:
        for sales in exp_sales: 
            print('Expected sales for a period of {0} months for {1}:${sales}'.format(t_hor, prod, sales = sales*t_hor))
            
#nested loops are considered are non-pythonic which means that it can be written better to follow the strucutre of python code rather than how its currently written

