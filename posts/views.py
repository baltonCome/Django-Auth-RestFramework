from urllib import response
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):

    if request.method == "POST":
        response= {"message": "Data Saved", "data": request.data}
        return Response (data=response, status=status.HTTP_201_CREATED)

    response= {"message":"Hello World"}
    return Response(data=response, status=status.HTTP_200_OK) 


@api_view(http_method_names=["GET"])
def list_posts(request:Request):
    return Response()



@api_view(http_method_names=["GET"])
def post_details(request:Request, post_index:int):
    return Response()
