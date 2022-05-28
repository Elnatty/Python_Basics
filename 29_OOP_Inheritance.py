'''
OOP by NAVIN (youtuber).

'''

class A:    # Super/Parent class
    def feature1(self):
        print('Feature 1 Working..')
    def feature2(self):
        print('Feature 2 Working..')

class B(A):    # Child/Sub class of class A
    def feature3(self):
        print('Feature 3 Working..')
    def feature4(self):
        print('Feature 4 Working..')

class C(B):    # Child/Sub class of B
    def feature5(self):
        print('Feature 5 Working..')

class D():
    def feature6(self):
        print('Feature 6 Working..')

class E():
    def feature7(self):
        print('Feature 7 Working..')

class F(D, E):  # inherits D and E.
    def feature8(self):
        print('Feature 8 Working..')

a1 = A()
a1.feature1()
a1.feature2()

# SINGLE-LEVEL Inheritance (B inherits A)
b1 = B()
# b1.feature1()

# MULTI-LEVEL Inheritance. (C inherits A and B)
c1 = C()
#c1.feature1(), c1.feature2(), c1.feature3(), c1.feature4(), c1.feature5()

# MULTIPLE inheritance
f1 = F()
# f1.feature6(), f1.feature7(), f1.feature8()