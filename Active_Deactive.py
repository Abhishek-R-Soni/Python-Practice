#   Active & Deactive User

class Facebook:
    active = 0
    def __init__(self,name):
        self.name = name
        Facebook.active += 1

    def online(self):
        print(f"{self.name} is Online now")
    
    def logout(self):
        self.active -= 1
        print(f"{self.name} is logged out")

user1 = Facebook("Abhishek")
user1.online()
user2 = Facebook("Dhimant")
user2.online()
user3 = Facebook("Khushi")
user3.online()
print(f"Total User {Facebook.active}")
user1.logout()
print(f"Total User {Facebook.active}")
user3.logout()
print(f"Total User {Facebook.active}")


