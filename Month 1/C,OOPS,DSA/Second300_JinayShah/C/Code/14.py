class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def post_message(self, message):
        self.posts.append(message)
        print(f"Message posted by {self.username}: {message}")

    def view_timeline(self):
        print(f"\nTimeline for {self.username}:")
        for post in self.posts:
            print(post)


users = {}

while True:
    print("\nSocial Networking Application")
    print("1. Create User")
    print("2. Post Message")
    print("3. View Timeline")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        username = input("Enter your username: ")
        users[username] = User(username)
        print(f"User {username} created successfully.")
    elif choice == '2':
        username = input("Enter your username: ")
        if username in users:
            message = input("Enter your message: ")
            users[username].post_message(message)
        else:
            print("User not found. Please create a user first.")
    elif choice == '3':
        username = input("Enter your username: ")
        if username in users:
            users[username].view_timeline()
        else:
            print("User not found. Please create a user first.")
    elif choice == '4':
        print("Exiting the Social Networking Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")