from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    auther = models.CharField(max_length=50)
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    should_start_at = models.TimeField()
    should_finish_till = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

