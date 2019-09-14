class Student:
    def __init__(self,no=1,name="default"):
        self.no = no
        self.name = name
    def display(self):
        return self.name

class Teacher(Student):
    def __init__(self,occup):
        self.occup = occup

obj1 = Student(1,"Abhi")
obj2 = Teacher("MCA")
#print(obj1.no)
print(obj2.display())