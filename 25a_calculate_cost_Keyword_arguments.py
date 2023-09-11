def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")
#calc_cost(50, 5, 0.1)
#contains 3 pieces of information:
#50 -> total cost all order items
#5 -> shipping cost
#0.1 -> discount
#at first glance, this might be difficult to understand
#to make it readable, by using keyword arguments
#calc_cost(total=50, shipping=5, discount=0.1)
#keyword arguments should always come after positional arguments
#greet_user(first="John", "Smith") returns error
greet_user("John", last_name="Smith")
print("Finish")