from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    link = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "posts")

    def __str__(self) -> str:
        return self.title