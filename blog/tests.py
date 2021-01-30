from django.test import TestCase
from .models import Author, BlogPost
from django.contrib.auth.models import User


class AuthorModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='aliakbar')
        
    def test_author_name(self):
        author = Author.objects.get(id=1)
        expected_name = 'aliakbar'
        self.assertEqual(expected_name, author.name)
        
        
class BlogPostModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        
        test_blogpost = BlogPost.objects.create(
            title='linux containers',
            body='containers are ...',
            author=testuser1
        )
        test_blogpost.save()
        
    def test_blogpost_content(self):
        blogpost = BlogPost.objects.get(id=1)
        expected_author = 'testuser1'
        expected_title = 'linux containers'
        expected_body = 'containers are ...'
        self.assertEqual(expected_author, blogpost.author)
        self.assertEqual(expected_body, blogpost.body)
        self.assertEqual(expected_title, blogpost.title)