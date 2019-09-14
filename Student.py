class Student:
    def __init__(self,fname,lname,no,city,age):
        self.fname = fname
        self.lname = lname
        self.no = no
        self.city = city
        self.age = age

    def dis(self):
        print(f"Name : {self.fname} {self.lname}\nNo : {self.no}\nCity : {self.city}\nAge : {self.age}")

    def goto_hell(self):
        print(f"{self.fname[0]}{self.lname[0]}")
        print(self.age > 50)

obj = Student("Abhi","Soni",49,"Baroda",60)
obj.dis()
obj.goto_hell()
        
