'''
OOP by NAVIN (youtuber).
'''

class Computer:
    # constructor.
    def __init__(self):
        self.name = 'Nathan'
        self.age = 25

    def compare(self, others):
        if self.age == others.age:
            return True
        return False

# to call a class, 1st create an object for the class.
c1 = Computer()
c2 = Computer()

# we can change the values for the self object.
c1.name = 'Moses'
c1.age = 30

# to compare both computers.
if c1.compare(c2):  # c1 represents 'self' while c2 represents others. We then call the compare method to compare them.
    print('They are same.')
else:
    print('They are different.')

# print(c1.name)
# print(c2.name)