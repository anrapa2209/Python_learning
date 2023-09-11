course = 'Python for Beginners'
print(len(course))                  #string length
print(course.upper())               #to convert to upper case
print(course.lower())               #to convert to lower case
print(course.title())
print(course.find('B'))             #to get the first appearance of that character
print(course.find('b'))             #returns -1 because there is no lower case b anywhere in the string
print(course.find('Beginners'))     #returns 11 because this word starts at index 11
print(course.replace('Beginners','Absolute Beginners'))
print(course.replace('beginners','Absolute Beginners')) #case sensitive, so no replacement
print(course.replace('P','J'))
print('Python' in course)
#in operator represents Boolean value, do we have this character or not
print('python' in course)

