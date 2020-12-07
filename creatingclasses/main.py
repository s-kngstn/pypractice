#When naming a Class make sure to have every name Capitalized 'LikeThisOk'
#This is called pascal case
class  User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
#Creating an Object 
user_1 = User("007", "James Bond")

#Creating an attribute
#an attribute is a Variable thats associated with an Object

print(user_1.username)
print(user_1.id)
print(user_1.followers)

user_2 = User("008", "James Pond")

print(user_2.username)
print(user_2.id)

#REMEMBER: Attributes are things the Object HAS, while Methods are the things the Object DOES

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)