'''
OOP by Navin..
Operator overloading Polymorphism
'''

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    # the __add__ represents addition..
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
    # the __gt__ rep greater-than..
    def __gt__(self, other):
        a1 = self.m1 + self.m2
        a2 = other.m1 + other.m2
        # condition check.
        if a1 > a2:
            return True
        else:
            return False

s1 = Student(58, 69)
s2 = Student(65, 65)
s3 = s1 + s2
# we can now overload the sum operation
# print(s3.m1)
# to check if s1 > than s2
if s1 > s2:
    print('S1 is greater..')
else:
    print('s2 is greater..')