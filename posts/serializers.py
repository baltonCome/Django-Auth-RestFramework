from dataclasses import fields
from turtle import title
from rest_framework import serializers
from . models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created']