# class example

class User:
    def __init__(self,name):
        self.name = name
        print(f"A new user {name}")

user = User("Abhi")
print(user.name)

