class User:
    def __init__(self, id):
        self.id = id
        self.posts = []
        self.followers = []

    def publish(self, post):
        self.posts.append(post)

    def follow(self, user):
        self.followers.append(user)


class Post:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.likes = 0

    def like(self):
        self.likes += 1


class Network:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.id] = user

    def find_influential_users(self):
        influential_user = max(self.users.values(), key=lambda u: sum(p.likes for p in u.posts))
        return influential_user

    def find_popular_posts(self):
        popular_post = max((p for u in self.users.values() for p in u.posts), key=lambda p: p.likes)
        return popular_post

    def find_connection_patterns(self):
        return len(set(f for u in self.users.values() for f in u.followers))

network = Network()

user1 = User(1)
user2 = User(2)
user3 = User(3)

network.add_user(user1)
network.add_user(user2)
network.add_user(user3)

user1.follow(user2)
user2.follow(user3)
user3.follow(user1)

user1.publish(Post(1, "Hello from user1"))
user2.publish(Post(2, "Hello from user2"))
user3.publish(Post(3, "Hello from user3"))

user1.posts[0].like()
user2.posts[0].like()
user3.posts[0].like()

print("Influential users: ", network.find_influential_users().id)

print("Popular posts: ", network.find_popular_posts().id)

print("Connection patterns: ", network.find_connection_patterns())
