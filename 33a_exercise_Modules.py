#either ~
#import utils                   #Import entire module
#utils.find_max()

#or ~

#from utils import find_max

#numbers = [56, 80, 5, 9, 111, 22, 13]
# above line is not brought into the function find_max() in the module 'utils', coz this is where we create a list
#so somewhere in the program, we are going to create this list and pass it as an argument to the find_max() function

#max = find_max(numbers)
#but 'max' is already a pre-defined function in Python to find the largest of no.s
#print(max(numbers))            #built-in fn is overridden & executed; bad practise

from utils import find_max

numbers = [56, 80, 5, 9, 111, 22, 13]
maximum = find_max(numbers)
print(maximum)
#print(maximum(numbers)) is incorrect, as 'maximum' is already assigned to the function find_max() from the module 'utils'
#So, now maximum is just an integer, not a function & you cannot call an argument to an int object

#or:

# from utils import find_max

# numbers = [56, 80, 5, 9, 111, 22, 13]
# print(find_max(numbers))
