class User:
   def __init__(self, username):
       self.username = username
       self.friends = []
       self.posts = []

   def add_friend(self, friend):
       self.friends.append(friend)

   def post_message(self, message):
       post = Post(self, message)
       self.posts.append(post)
       for friend in self.friends:
           friend.receive_post(post)

   def receive_post(self, post):
       self.posts.append(post)

   def display_timeline(self):
       for post in self.posts:
           print(f"{post.author.username}: {post.message}")

class Post:
   def __init__(self, author, message):
       self.author = author
       self.message = message

class Friendship:
   def __init__(self, user1, user2):
       user1.add_friend(user2)
       user2.add_friend(user1)

# Create some users
user1 = User("User1")
user2 = User("User2")

friendship = Friendship(user1, user2)

user1.post_message("Hello, world!")

user1.display_timeline()