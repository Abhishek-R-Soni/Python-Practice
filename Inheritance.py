# Inheritance

class Person:
    def __init__(self,name,city):
       print("") 
    def __repr__(self,name,city):
        self.name = name
        self.city = city
        print(f"{self.name} lives in {self.city}")

class Student(Person):
    def __init__(self,name,city,desg):
        super().__repr__(name,city)
        self.desg = desg
    def __repr__(self):
        print(f"{self.name} has {self.desg}")
        
s = Student("Abhishek","Baroda","Dev")
print(s.__repr__())
