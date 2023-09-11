# class Dog:
#     def walk(self):
#         print("Walk")


# class Cat:                              #code is duplicated
#     def walk(self):
#         print("Walk")
# Programming has a DRY principle -> Don't Repeat Yourself


class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
#Dog class will inherit all the methods defined in the mammal class
    def bark(self):
        print("Bark")


class Cat(Mammal):
    pass            #written just coz Python doesn't like an empty class


dog1 = Dog()
dog1.walk()
dog1.bark()