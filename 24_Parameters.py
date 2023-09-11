def greet_user(first_name, last_name):
#here, (first_name, last_name) are the parameters
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")          #2 line breaks after defining function
greet_user("John", "Smith")
#here, ("John", "Smith") are the arguments
greet_user("Mary", "Cooper")
#we can take a few lines of code that perform a specific task and put them inside a function
#greet_user()               #will return an error
print("Finish")
