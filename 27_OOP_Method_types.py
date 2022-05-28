'''
OOP by NAVIN (youtuber).

--> Types of Methods in OOP:
    1: >>> Instance Method: works with the object, eg: def avg(self) --> to call it, s1.avg() because s1 is the object ie, (self).
            they can also be used with instance variables ie, (m1,m2,m3).

    2: >>> Class Method: works with class variables, eg: in line 24, def get_school(cls) works as class method, and works with class
            variables like in line 17, to use this we also use a special decorator ie: @classmethod.

    3: >>> Static Method: has nothing to do with Instance or Class Variables, with no self or cls arguments passed in them. eg: in
            line 31, def info(), to use this we also use a special decorator ie: @staticmethod.

    NOTES:
        -> if ur working with INSTANCE variable you use a (self) keyword.
        -> if ur working with CLASS variable you use a (cls) keyword.
'''

class Students:
    school = 'Zenith'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod    # we use decorators when we want to run 'get_school' as a Class Method.
    def get_school(cls):   # this is a Class Method.
        return cls.school

    @staticmethod
    def info():             # Static Method.
        print('This is student class.. in abc module..')

    # if you want to get the value of m1 or m2 or m3, you can use Getters/Accessors (they just fetch the values).
    # or you can just do: print(s1.m1) to get the mi value.
    def get_m1(self):
        return self.m1
    # if you want to set the value for m1 or m2 or m3, you can use Setters/Mutators (they change the values.)
    # or you can just do: s1.m1 = value, where value is your choice of number.
    def set_m1(self, value):
        self.m1 = value

    def avg(self):    # this is an Instance Method.
        return (self.m1 + self.m2 + self.m3) / 3

s1 = Students(20, 32, 43)
s2 = Students(41, 46, 29)

# print(s2.avg())
# s1.set_m1(100)

# calling the Class Method at line 23.
# print(s1.info())
# or
# print(Students.get_school())

# calling static method.
# Students.info()
# or
# s1.info()