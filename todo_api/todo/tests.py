from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        Todo.objects.create(auther='admin', title="test todo", \
            description="a description here", \
                should_start_at = '05:00:00', \
                    should_finish_till = '06:00:00')
    
    def test_user_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_user = f'{todo.auther}'
        self.assertEqual(expected_object_user, 'admin')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'test todo')

    def test_description_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_description = f'{todo.description}'
        self.assertEqual(expected_object_description, 'a description here')

    def test_should_start_at_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_time = f'{todo.should_start_at}'
        self.assertEqual(expected_object_time, '05:00:00')

    def test_should_finish_till_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_time = f'{todo.should_finish_till}'
        self.assertEqual(expected_object_time, '06:00:00')
