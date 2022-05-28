'''
OOP by NAVIN (youtuber).
Class --> is more like a blueprint, consisting of Attributes and Behaviours.
    Attributes: are variables.
    Behaviours: are methods/functions.

'''

# --> Example 1:
class Computer:
    # a method
    def config(self):
        print('i5, 16gb, 1TB')
# to call the method config.
# 1st way.
comp1 = Computer()
Computer.config(comp1)      # comp1 reps the (self) --> self is the object you are passing.
# 2nd way, most used way.
comp1.config()
