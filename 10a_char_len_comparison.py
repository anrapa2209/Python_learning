# conditions: if name is less than 3 characters long
#             name must be at least 3 characters
# otherwise if it's more than 50 characters long
#           name can be a maximum of 50 characters
# otherwise
#           name looks good!

char_name = 'Aparna Shankar'
if len(char_name) < 3:
    print('Name must be at least of three characters')
elif len(char_name) > 50:
    print('Name can be a maximum of fifty characters')
else:
    print('Name looks good')