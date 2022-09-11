from django.shortcuts import render
from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, ) #new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer