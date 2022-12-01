from dataclasses import fields
from turtle import title
from rest_framework import serializers
from . models import Post
from accounts.serializers import UserDataSerializer


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 50)
    
    class Meta:
        model = Post
        fields = ['id', 'title','topic', 'content', 'link', 'procedure', 'created']    



class PostWithUserSerializer(serializers.ModelSerializer):

    #Work on Queryset
    user_info = UserDataSerializer(source = 'author')
    
    class Meta:
        model = Post
        fields = ['id', 'title','topic', 'content', 'link', 'procedure', 'created', 'user_info']   