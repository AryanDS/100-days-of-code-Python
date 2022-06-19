#OPPs Introduction!
class User:
    def __init__(self,user_id, username):
        print("A new object is created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    #the method below will increase the follower and following of the user 
    def follow(self, user):
        user.followers+=1
        self.following+=1

#creating an object user1 of class User
user1 = User(1,"Aryan")

#Creating attributes of the object

print(f"the user name of the first object is {user1.username}")
print(user1.id)
print(user1.followers)


#creating a new user (object)
user2 = User(2,"Anushka")
print(f"the user name of the second object is {user2.username}")
print(user2.id)
print(user2.followers)

#calling the follow method
user1.follow(user2)

#checking whether the number of follower/following increases or not
print("The number of followers/following")
print(user2.followers)
print(user1.following)