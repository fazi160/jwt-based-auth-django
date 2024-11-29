from rest_framework import serializers
from .models import Blog, LikedBlogs

class BlogSerializers(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [  # Explicitly list all fields to avoid string-tuple concatenation issues
            *[f.name for f in Blog._meta.fields],  # All model fields
            'like_count'  # Add the custom field
        ]

    def get_like_count(self, obj):
        # Count the number of likes for the given blog
        return LikedBlogs.objects.filter(blog=obj).count()

class LikedBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikedBlogs
        fields = '__all__'

