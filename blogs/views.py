from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializers
from backend.permissions import AuthorPermission, AuthorEditPermission, UserPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        action_permissions = {
            'create': [AuthorPermission],
            'update': [AuthorEditPermission],
            'partial_update': [AuthorEditPermission],
            'destroy': [AuthorEditPermission],
            'list': [UserPermission],
            'retrieve': [UserPermission],
        }
        # Assign appropriate permissions based on the action
        self.permission_classes = action_permissions.get(self.action, [UserPermission])
        return super().get_permissions()


class BlogLikeView(APIView):
    permission_classes = [UserPermission]

    def post(self, request, *args, **kwargs):
        user = request.user  
        blog_id = request.data.get('blog')

        if not blog_id:
            return Response({"error": "Blog ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)

        liked_blog, created = LikedBlogs.objects.get_or_create(blog=blog, user=user)

        if created:
            return Response({"message": "Blog liked successfully."}, status=status.HTTP_201_CREATED)
        
        liked_blog.delete()
        return Response({"message": "Blog unliked successfully."}, status=status.HTTP_200_OK)
