from rest_framework import serializers
from blog.models import Author, BlogPost, Comment
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'body', 'date_created')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('blog_post', 'text')