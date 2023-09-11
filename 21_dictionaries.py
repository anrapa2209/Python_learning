#conditions, when each attribute has a value
#Name: John Smith
#Email: john@gmail.com
#Phone: 1234

customer = {
    "name": "John Smith",                                   #key: value pair, separate 2 key:value pairs by a ','
    "age": 30,
   #"age": 40,                                               age is highlighted as it is duplicated & hence, is_verified cannot be True
    "is_verified": True
}
#key should be unique, cannot be duplicated
#value can be anything: string, boolean, int or even a list
print(customer["name"])                                     #printing the value associated with the 'name' key
print(customer.get("name"))                                 #to use () instead of []
#print(customer["birthdate"])                                pathing a key that doesn't exist gives a key error
#print(customer["Name"])                                     case-sensitive
print(customer.get("birthdate"))                            #returns 'NONE' value, safer than above as it doesn't give error
print(customer.get("birthdate", "January 1 1980"))          #to optionally supply a default value, when the dictionary doesn't have a particular key
#to update any of the above values:
customer["name"] = "Jack Smith"
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])