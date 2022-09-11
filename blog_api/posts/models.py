from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name_plural = 'posts'
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


