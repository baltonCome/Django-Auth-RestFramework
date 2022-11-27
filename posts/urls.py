from . import views
from django.urls import path



urlpatterns = [
    path("new", views.PostCreateView.as_view() , name="create_posts"),
    path(
        "<int:pk>/", 
        views.PostRetrieveUpdateDeleteView.as_view(), 
        name="post_detail"
    ),
    path("all", views.postWithUser , name="get_posts_with_users"),
]