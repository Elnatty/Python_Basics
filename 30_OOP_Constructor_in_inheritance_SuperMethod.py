'''
OOP by NAVIN (youtuber).
THe Super Method.
'''

class A:
    def __init__(self, a):
        self.a = a
        # print('Init A is working..')
    def featureA(self):
        print('Feature A Working..')

class B(A):
    def __init__(self, a):
        super().__init__(a)
    def feat(self):
        print(f'Init B is working.. with init A argument: {self.a}')
        # using super(). to call class A method
        super().featureA()

# to call the init method of class A, we use the super().__init__ to call it since class B is a subclass of A.
# we can also use the super(). to call other super class methods too
a1 = B('A')
a1.feat()
# But when you have multiple inheritance, ie a class C(A, B). Tis will call the init method of class A and C omly.