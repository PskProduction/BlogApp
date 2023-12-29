from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'created_at')


class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'created_at', 'comments')

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        return CommentSerializer(comments, many=True).data

