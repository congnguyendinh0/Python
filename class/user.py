class User:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1
user_1 = User("1","Cong")

print (user_1.name)
print (user_1.followers)


 