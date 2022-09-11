from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'auther', 'title', 'content', 'created_at', 'updated_at')
        model = Post
