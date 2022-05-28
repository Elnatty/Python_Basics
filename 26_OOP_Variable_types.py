'''
OOP by NAVIN (youtuber).

--> Types of Variables in OOP:
    1: >>> Instance Variable: are variables that are defined inside the __init__ method and can be changed, eg:
            self.mileage and self.company.
    2: >>> Class/Static Variable: are variables that are not inside the __init__ method, and can also be changed.
'''

class Car:
    wheels = 4                # CLass variables

    def __init__(self):
        self.mileage = 10     # instance variable
        self.company = 'BMW'  # instance variable

c1 = Car()
c2 = Car()
# changing the value for c1 (instance variable)
c1.mileage, c1.company = 20, 'Royce'
# changing the value for wheels (class variable)
Car.wheels = 5

print(c1.mileage, c1.company, c1.wheels)
print(c2.mileage, c2.company, c2.wheels)