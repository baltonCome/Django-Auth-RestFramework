from dataclasses import fields
from turtle import title
from rest_framework import serializers
from . models import Post, User
from accounts.serializers import CurrentUserPostsSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 50)

    user_info = CurrentUserPostsSerializer(source = 'author')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'link', 'procedure', 'created', 'user_info']