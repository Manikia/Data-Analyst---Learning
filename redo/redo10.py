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
