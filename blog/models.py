from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    text = models.CharField(max_length=500)
    blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    