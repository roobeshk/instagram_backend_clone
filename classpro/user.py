class User:
    def __init__(self, user_id, user_name, bio):
        self.user_id = user_id
        self.user_name = user_name
        self.bio = bio
        self.posts = []
        self.following = []