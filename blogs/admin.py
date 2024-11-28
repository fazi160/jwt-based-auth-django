from django.contrib import admin
from .models import Blog, LikedBlogs
# Register your models here.
admin.site.register(Blog)
admin.site.register(LikedBlogs)
