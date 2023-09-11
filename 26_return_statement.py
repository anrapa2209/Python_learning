#how to create functions that return values to the callers of the function:
def square(number):
    return number * number
    #print(number * number)             #instead of the above, if you give this print() directly without a return statement, Python returns a default NONE value
#to return the square value outside of this function, we need to provide a return statement


#result = square(13)           #same as input function
#print(result)
print(square(13))              #to reduce the line of code
#by default, all functions in Python return NONE, to change that we need a return  statement