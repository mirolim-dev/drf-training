from tkinter.filedialog import test
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
       testuser1 = User.objects.create_user(username='admin2', password='admin2')
       testuser1.save()


       test_post = Post.objects.create(auther=testuser1, title='Blog title', content="Body content")
       test_post.save()


    def test_blog_content(self):
        post = Post.objects.get(id=1)
        auther = f'{post.auther}'
        title = f'{post.title}'
        content = f'{post.content}'

        self.assertEqual(auther, 'admin2')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(content, 'Body content')