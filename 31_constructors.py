class Point:
    def __init__(self, x, y):
    #__init__ short for initialized, a fn.that gets called when we create a new point object
        self.x = x          #self is a reference to the current object
        self.y = y

    def move(self):                         #defining a function to move a point
        print('move')

    def draw(self):
        print('Draw')


#point1 = Point()
#print(point1.x)
#without def __init__ function, this print returns Attribute error, which is a problem
# It is possible to have a Point object x or y coordinate.
# To solve this problem, we use a contructor - a function that gets called at the time of creating an object

point = Point(10, 20)
point.x = 11
print(point.x)
