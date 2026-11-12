class Post:
    def __init__(self, post_id, caption):
        self.post_id = post_id
        self.caption = caption
        self.likes = 0
        self.comments = []
