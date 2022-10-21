from . import views
from django.urls import path

urlpatterns = [
    path("homepage", views.homepage, name="posts_home"),
    path("list_posts", views.list_posts, name="list_posts"),
    path("list_posts/<int:post_id>", views.post_details, name="post_details")
] 