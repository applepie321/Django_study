from django.db import models

class Post(models.Model):
    title = models.CharField("Post title", max_length=100)
    content = models.TextField("Post content")
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("Comment")
    
    def __str__(self):
        return f"{self.post.title} comment from (ID: {self.id})"
