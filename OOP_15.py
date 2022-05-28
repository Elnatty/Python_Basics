# This is our super class
class Car(object):
    # constructor
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        # constance can also be added too..
        self.static = 'constant car data'
        # print('This is to check if the constructor is working...')
    def __int__(self):
        return f'Car is from {self.year}'
    def __str__(self):
        return f'String representation: {self.year} {self.make} {self.model}'
    def printcar(self):
        '''echoes back the full name of the vehicle'''
        print(f'{self.year} {self.make} {self.model}')
        print(self.static)


# This is our sub class... inherits attributes from super class (car)
# class Bike(Car):
#     pass
# ns = Bike('1990', 'Nissan', 'Sentra')
# print(ns.printcar())