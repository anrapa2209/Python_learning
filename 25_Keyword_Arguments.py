def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")          #2 line breaks after defining function
greet_user("John", "Smith")
#here, ("John", "Smith") are arguments,
#here John & Smith are Positional arguments, i.e. their position or order matters
#first argument is the value to the first parameter, 2nd argument is the value to the second parameter & so on.
greet_user("Smith", "John")
#but in keyword arguments, the position doesn't matter
#greet_user("Smith", first_name="John")             #error, since there are 2 values for first_name as Smith is also defaulted to first_name
greet_user(last_name="Smith", first_name="John")
print("Finish")
