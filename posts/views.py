from email import message
from urllib import response
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from . models import Post
from . serializers import PostSerializer
from django.shortcuts import get_object_or_404

from posts import serializers

# Create your views here.

@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):

    if request.method == "POST":
        response= {"message": "Data Saved", "data": request.data}
        return Response (data=response, status=status.HTTP_201_CREATED)

    response= {"message":"Hello World"}
    return Response(data=response, status=status.HTTP_200_OK) 


class PostListCreateView(APIView):
    serializer_class = PostSerializer

    def get(self, request:Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many = True)

        return(Response(data=serializer.data, status=status.HTTP_200_OK))

    def post(self, request:Request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message" : "Post Saved",
                "data" : serializer.data 
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer

    def get(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)
        serializer = self.serializer_class(instance=post)

        return Response (data = serializer.data, status=status.HTTP_200_OK)

    def put(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)
        data = request.data
        serializer = self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message" : "Data Updated",
                "data" : serializer.data
            }

            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)

        post.delete()

        return Response(status.HTTP_204_NO_CONTENT)

    