'''
OOP by NAVIN (youtuber).

'''

class Student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber
        # to use inner class, you have to create the object of the class name which is in line 15.
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollnumber)
        self.lap.show()

    # class inside the Student class.
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Moses', 2)
s2 = Student('James', 3)
# print(s1.name, s1.rollnumber)
# s2.show()

# to call the inner class.
lap1 = Student.Laptop
lap2 = Student.Laptop
s1.show()