class A:
    def f1(self):
        print("In A")
class B:
    def f1(self):
        print("In B")
class C(B,A):
    def f3(self):
        print("In C")
        
u = C()
#print(u.f2())
print(u.f1())
print(u.f3())
