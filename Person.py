class Person:
    def __init__(self,name,mob,city):
        self.name = name
        self.mob = mob
        self.city = city

    def dis(self):
        print(f"Name : {self.name}\nMob :{self.mob}\nCity : {self.city}")

class Student(Person):
    def __init__(self,name,mob,city,no):
        super().__init__(name,mob,city)
        self.no = no

    def show(self):
        print(self.no)

s = Student("Abhi",9662046805,"Baroda","MA049")
s.dis()
s.show()
