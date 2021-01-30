from django.urls import path
from .views import (
    AuthorListAPIView, AuthorChangeAPIView,
    BlogPostChangeAPIView, BlogPostListCreateAPIView
)

urlpatterns = [
    path('author/', AuthorListAPIView.as_view()),
    path('author/<int:pk>/', AuthorChangeAPIView.as_view()),
    path('blogpost/', BlogPostListCreateAPIView.as_view()),
    path('blogpost/<int:pk>/', BlogPostChangeAPIView.as_view()),
]