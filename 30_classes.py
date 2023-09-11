#basic types in Python: Numbers, Strings, Boolean
#complex types: Lists, Dictionaries
#now think of a shopping cart, it is not any of the above, we need Classes to model real concepts
numbers = [1, 2, 3]
#point.move, point.draw, point.get_distance
#class Point
#Point is the name given to this particular class
#It has P in caps, based on the Pascal naming convention.
# For variables & functions, we always use lower case letters & separate multiple words using an _
# but in classes, each word is started with a capital letter, no spaces, for eg.
#class EmailClient
class Point:
    def move(self):                         #defining a function to move a point
        print('move')

    def draw(self):
        print('Draw')

                                            #2 line breaks after function
#with this class, we created new types, with these types, we need to create new objects
#an object is an instance of a class and a class defines a template for creating objects
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)                     #prints x coordinate of point 1
point1.draw()

point2 = Point()
point2.x = 1
#without the above line, the below print returns 'Attribute error', since point2 doesn't have an attribute called x
print(point2.x)
