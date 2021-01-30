from django.contrib import admin
from .models import BlogPost, Author, Comment
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Comment)