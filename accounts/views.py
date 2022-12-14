import email
from email import message
from lib2to3.pgen2 import token
from urllib import response
from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from rest_framework.decorators import api_view, APIView, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.

@permission_classes([AllowAny])
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"User saved",
                "data" : serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class LoginView(APIView):
    
    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message" : "Logged",
                "tokens" : tokens
            }
            return  Response(data=response, status= status.HTTP_200_OK)
        else:
            return Response(data={"message": "Bad Credentials"}, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request:Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=content, status = status.HTTP_200_OK)