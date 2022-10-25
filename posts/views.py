from email import message
from urllib import response
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from . models import Post
from . serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from posts import serializers

# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  
