# PROJECT 10 — Instagram Backend
# Create the following classes
# User Class

# Attributes:

# user_id

# user_name

# bio

# Post Class

# Attributes:

# post_id

# caption

# likes

# Comment Class

# Attributes:

# comment_id

# comment_text

# InstagramService Class

# Methods:

# create_user()

# create_post()

# like_post()

# comment_post()

# follow_user()

# show_feed()

# Requirements

# A user can create multiple posts.

# Increase the like count when a post is liked.

# Store comments for each post.

# Show posts from followed users in the feed.

# Menu

# Create User

# Create Post

# Like Post

# Comment Post

# Follow User

# Show Feed

# Exit
from instragramservice import InstagramService

instagram = InstagramService()

while True:

    print("\n===== INSTAGRAM BACKEND =====")
    print("1. Create User")
    print("2. Create Post")
    print("3. Like Post")
    print("4. Comment Post")
    print("5. Follow User")
    print("6. Show Feed")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        instagram.create_user()

    elif choice == "2":
        instagram.create_post()

    elif choice == "3":
        instagram.like_post()

    elif choice == "4":
        instagram.comment_post()

    elif choice == "5":
        instagram.follow_user()

    elif choice == "6":
        instagram.show_feed()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
