#lambda functions: is a syntax to creating anaonymous functions

#in cases where we dont want to define the whole functions we can use the lambda fucntion
#we can create a function that will focus on the function itself which will be an anonymous function

def raise_to_the_power_of_2(x):
    return x**2
raise_to_the_power_of_2(3)

#now in lambda form:
lambda_ex = lambda x:x**2
print(lambda_ex(3))

#we can also write lambda in its own argument like so:
print((lambda x:x**2)(3))

#lambdas can also have multiple parameters
sum_xy = lambda x,y:x+y
print(sum_xy(2,3))

#we can also create a fuinction where y(x) we have to create another function for the y in y(x). in these type of numberic we can let x be a numeric value but y has to be a function
sum_xy = lambda x,y : x+y(x)
print(sum_xy(2, lambda x: x*5))


