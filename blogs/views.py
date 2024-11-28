from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Blog, LikedBlogs
from .serializers import BlogSerializers, LikedBlogSerializers
from utils.decorators import custom_auth_required


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    def get_queryset(self):
        return Blog.objects.all()

    @custom_auth_required(user_types=['author'], allow_owner_only= True)
    def list(self, request, *args, **kwargs):
        # Handle GET requests for listing all blogs
        return super().list(request, *args, **kwargs)

    @custom_auth_required(user_types=['author'])
    def create(self, request, *args, **kwargs):
        # Only authors can create new blogs
        return super().create(request, *args, **kwargs)

    @custom_auth_required(user_types=['author'], allow_owner_only=True)
    def update(self, request, *args, **kwargs):
        # Only the owner (blogger) can update their blog
        return super().update(request, *args, **kwargs)

    @custom_auth_required(user_types=['author'], allow_owner_only=True)
    def destroy(self, request, *args, **kwargs):
        # Only the owner (blogger) can delete their blog
        return super().destroy(request, *args, **kwargs)


class BlogUserView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    @custom_auth_required(user_types=['user', 'admin'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BlogLikeView(APIView):

    @custom_auth_required(user_types=['user'])
    def post(self, request, *args, **kwargs):
        user = request.user  # Authenticated user
        blog_id = request.data.get('blog')  # Blog ID from request data

        if not blog_id:
            return Response({"error": "Blog ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the blog is already liked by the user
        liked_blog, created = LikedBlogs.objects.get_or_create(
            blog=blog, user=user)

        if created:
            # If a new entry is created, it's a "like" action
            return Response({"message": "Blog liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            # If the entry already exists, it's an "unlike" action
            liked_blog.delete()
            return Response({"message": "Blog unliked successfully."}, status=status.HTTP_200_OK)



