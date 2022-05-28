'''
OOP by NAVIN (youtuber).
--> The __init__ method:
        the __init__ method gets called automatically.
'''

# --> Example 2:
class Computer:
    def __init__(self, cpu, ram):   # cpu and ram are arguments.
        self.cpu = cpu  # self.cpu is an object for the cpu argument.
        self.ram = ram  # self.ram is an object for the ram argument.

    # a method of the class Computer.
    def config(self):
        print('Config is ', self.cpu, self.ram)

# to call, we have 2 computers: comp1 and comp2, which are objects.
comp1 = Computer('i5', 16)       # computer 1 with its specs, cpu and ram.
comp2 = Computer('Ryzen 3', 8)   # computer 2 with its specs, cpu and ram.

comp1.config()
comp2.config()