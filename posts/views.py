from email import message
from urllib import response
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from . models import Post
from . serializers import PostSerializer, PostWithUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from accounts.serializers import CurrentUserPostsSerializer
from posts import serializers
from .permissions import ReadOnly, AuthorOrReadOnly

# Create your views here.
#Man i sincerely hope you remember this, but here is the deal... There are two different serializers for each type of request. Because for POST you don't need to indicate the user cuz it comes with the request, but for GET you need a serializer that clarify that you are getting the post with the user.

#Hi there, this note is to clarify that beside having created many views, not all were implemented in the urls.

class PostCreateView(
    generics.GenericAPIView,
    mixins.CreateModelMixin
):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author = user)
        serializer.save()
        return super().perform_create(serializer)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = PostWithUserSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request : Request):
    user = request.user
    
    serializer = CurrentUserPostsSerializer(
        instance=user,
        context = {"request" : request}
    )

    return Response(
        data=serializer.data,
        status= status.HTTP_200_OK
    )
  

class ListPostsForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Post.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def postWithUser(request:Request):

    posts = Post.objects.order_by('-created')
    serializer = PostWithUserSerializer(instance=posts, many = True)
    response = {
        "message" : "Posts",
        "data" : serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)

