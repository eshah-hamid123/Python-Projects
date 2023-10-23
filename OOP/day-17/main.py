class User:

    def __init__(self , user_id , user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow_data(self, user):
        self.followers += 1
        user.following += 1


user1 = User('001', 'Eisha')
user2 = User('002', 'Fatima')
# user1.name = 'Eisha'
user1.follow_data(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

