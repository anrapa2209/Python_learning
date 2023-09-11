#how to use one of the built-in Python modules to generate random values:

import random               #find source file in external libraries -> python library root -> xmlrpc

for i in range(3):          #range function is used to create a range of objects, we can look thru this range of objects and in each iteration, this object will spin out a value
    print(random.random())
    # generates any 3 random values btwn 0 to 1, everytime we call this function
    print(random.randint(10, 20))
    # generates any 3 random integer values btwn 10 to 20
# dot operator '.' is to access the module's methods
