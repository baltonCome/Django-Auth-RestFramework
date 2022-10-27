from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ["created"]  