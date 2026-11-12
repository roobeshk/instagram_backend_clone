from user import User
from post import Post
from comment import Comment

class InstagramService:


    def __init__(self):
        self.users = []
        self.posts = []
        self.post_owner = {}

    def create_user(self):
        user_id = int(input("Enter User ID: "))
        user_name = input("Enter User Name: ")
        bio = input("Enter Bio: ")

        user = User(user_id, user_name, bio)
        self.users.append(user)

        print("User created successfully!")

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user

    def find_post(self, post_id):
        for post in self.posts:
            if post.post_id == post_id:
                return post

    def create_post(self):
        user_id = int(input("Enter User ID: "))
        user = self.find_user(user_id)

        if user:
            post_id = int(input("Enter Post ID: "))
            caption = input("Enter Caption: ")

            post = Post(post_id, caption)

            user.posts.append(post)
            self.posts.append(post)
            self.post_owner[post_id] = user

            print("Post created successfully!")
        else:
            print("User not found!")

    def like_post(self):
        post_id = int(input("Enter Post ID: "))
        post = self.find_post(post_id)

        if post:
            post.likes += 1
            print("Post liked successfully!")
            print("Total Likes:", post.likes)
        else:
            print("Post not found!")

    def comment_post(self):
        post_id = int(input("Enter Post ID: "))
        post = self.find_post(post_id)

        if post:
            comment_id = int(input("Enter Comment ID: "))
            comment_text = input("Enter Comment: ")
            user_name = input("Enter Your Name: ")

            comment = Comment(
                comment_id, comment_text, user_name
            )

            post.comments.append(comment)

            print("Comment added successfully!")
        else:
            print("Post not found!")

    def follow_user(self):
        user_id = int(input("Enter Your User ID: "))
        user = self.find_user(user_id)

        if user:
            follow_id = int(input("Enter User ID to Follow: "))
            follow = self.find_user(follow_id)

            if follow and follow != user:
                if follow not in user.following:
                    user.following.append(follow)
                    print("User followed successfully!")
                else:
                    print("Already following this user!")
            else:
                print("Invalid user!")
        else:
            print("User not found!")
  
    def show_feed(self):
        user_id = int(input("Enter Your User ID: "))
        user = self.find_user(user_id)

        if user:
            print("\n===== INSTAGRAM FEED =====")

            if not user.following:
                print("You are not following anyone!")
                return

            for followed_user in user.following:
                for post in followed_user.posts:
                    print("\nPost ID:", post.post_id)
                    print("Username:", followed_user.user_name)
                    print("Caption:", post.caption)
                    print("Likes:", post.likes)

                    print("Comments:")
                    for comment in post.comments:
                        print(comment.user_name, ":", comment.comment_text)
        else:
            print("User not found!")

    