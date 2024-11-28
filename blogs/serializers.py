from rest_framework import serializers
from .models import Blog, LikedBlogs

class BlogSerializers(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'  # Include all fields from the Blog model
        fields += ('like_count',)  # Add like_count to the serialized output

    def get_like_count(self, obj):
        # Count the number of likes for the given blog
        return LikedBlogs.objects.filter(blog=obj).count()

class LikedBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikedBlogs
        fields = '__all__'

