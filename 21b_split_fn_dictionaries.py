message = input(">")            #an input string
#to split the string by a space, eg. break the string 'Good morning :)' into 3 words:
words = message.split(' ')
#the above method goes thru a string & anywhere it finds the defined character, i.e.
#in this case ' ' (a space), it uses it as a boundary to separate the string into multiple words
#& then, it returns a list
print(words)
