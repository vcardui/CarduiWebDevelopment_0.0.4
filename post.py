import requests

class Post:
    def __init__(self, id):
        self.id = int(id) - 1

        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        blog_response = requests.get(blog_url)
        all_posts = blog_response.json()

        self.title = all_posts[self.id]["title"]
        self.subtitle = all_posts[self.id]["subtitle"]
        self.body = all_posts[self.id]["body"]

        # print(f"self.title = {self.title}")
        # print(f"self.subtitle = {self.subtitle}")
        # print(f"self.body = {self.body}")