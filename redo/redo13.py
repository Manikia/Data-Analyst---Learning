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

    #off topic that it didnt cover but it uses in the exercise is filtering a list
    #filtering is uses by passing a parameter and returning only what is true
    #ex:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # returns True if number is even
def check_even(number):
    if number % 2 == 0:
        return True  
    return False
    # Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)
    # converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)
    # Output: [2, 4, 6, 8, 10]


#data gathering and data collection
#two types of data primary and secondary
#primary data is data we create like a survey
#secondary data is existing data tha someone has gathered
#to get data from online that isnt in a downloadable file we can do web scraping or API
#web scraping is when we extract info w code from websites and we extract the data we want ex: a youtube vid that checks the views and is updating is webscraping
#APIs are designed for program data exchange


