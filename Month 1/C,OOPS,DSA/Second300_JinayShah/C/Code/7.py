posts = []

def display_posts():
    if not posts:
        print("No posts available.")
    else:
        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post}")

def create_post():
    title = input("Enter the post title: ")
    post = f"{title}"
    posts.append(post)
    print("Post created successfully.")

while True:
    print("\nSimple Blogging Platform")
    print("1. Display Posts")
    print("2. Create Post")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        display_posts()
    elif choice == '2':
        create_post()
    elif choice == '3':
        print("Exiting the blogging platform. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
