numbers = [5, 2, 1, 7, 4]
print(numbers)
numbers.append(13)                      #to add a number to the end of the list
print(numbers)
numbers.insert(2, 20)                   #to insert a number in between the list
print(numbers)
numbers.remove(5)                       #to remove an item from the list
print(numbers)
numbers.pop()                           #to remove the last item from the list
print(numbers)
print(numbers.index(20))                #check existence of an item in the list
#in operator to check the existence of an item in a list
print(50 in numbers)
#print(numbers.index(5))                #this method generates an error, safer to use in operator
numbers.clear()                         #to remove all items from the list
print(numbers)
print('')
#to count the occurrences of an item
numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))
# print(numbers.sort())
#'NONE'is an object in python that represents absence of a value
# Directly printing a number.sort() will return NONE
numbers.sort()
print(numbers)                          #items sorted in ascending order
numbers.reverse()
print(numbers)                          #items sorted in descending order
numbers2 = numbers.copy()
numbers.append(10)                      #no impact of this command, since copy() provides copy of original list
print(numbers2)                         #to get a copy of the original list

