class Person:
    def __init__(self, name):           #constructor
        self.name = name                #'self' references the current object
#we set the name argument of the current object to the name argument passed to this method

    def talk(self):
        print('talk')
        print(f"Hi, I am {self.name}")


john = Person('John Smith')
#print(john.name)               #not needed now
john.talk()

bob = Person('Bob Smith')
bob.talk()