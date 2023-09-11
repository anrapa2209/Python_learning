#Task~
# define a class called dice
# in this class, we have a method called roll();
# everytime we call this method, we get a tuple (i.e., a read-only list, that cannot be changed)
# everytime we call the roll method, we should get a tuple of 2 random values

import random


class Dice:
    #PEP8 is an enhancement-proposal document that has all best practices for formatting our code
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second            #Python automatically interprets this as a tuple
        # in Python, when you want to return a tuple from a function, you don't need (), so no need to use 'return (first, second)'


dice = Dice()
print(dice.roll())