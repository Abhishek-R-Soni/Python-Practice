# experiment

class Test:
    count = 0
    def __init__(self):
        self.count += 1
        self.dis_count()
        
    def dis_count(self):
        return self.count

user1 = Test()

print(Test.count)
