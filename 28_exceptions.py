#how to handle errors in Python programs:

#age = int(input("Age: "))               #input("Age: ") defaults to a string, we need to convert it to int
#print(age)
#The terminal gives the message, 'Process finished with exit code 0':
# exit code 0 means the program terminated successfully with no errors
#if you input anything other than an integer, for eg., asd, you will get a 'Value Error'
#and the exit code is now 1, i.e., the program crashed
#but we don't want the entire prog to crash just because the user entered an invalid value
#so instead, we should handle the sitn. & print a proper error message. How? #try #except
#Exception is a kind of error that crashes our program
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')
    #ensures that exit code is 0 even despite a value error, i.e., program was executed successfully
