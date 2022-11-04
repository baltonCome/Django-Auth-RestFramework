from email.mime import base
from django.contrib import admin
from django.urls import path, include
#from posts.views import PostViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#router.register("", PostViewset, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('auth/', include("accounts.urls")),        
]