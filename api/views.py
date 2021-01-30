from rest_framework import generics, permissions
from blog.models import Author, BlogPost, Comment
from .serializers import AuthorSerializer, BlogPostSerializer
from django.contrib.auth.models import User

class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
class AuthorChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    
class BlogPostChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return BlogPost.objects.filter(author=user)
    
    

