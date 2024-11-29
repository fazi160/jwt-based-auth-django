from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from backend.permissions import AdminPermission


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AdminAuthorView(APIView):
    permission_classes = [AdminPermission]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')

        # Validate required fields
        if not user_id:
            return Response(
                {"error": "'user_id' field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Toggle the is_permitted value
        user.is_permitted = not user.is_permitted
        user.save()

        action = "granted" if user.is_permitted else "revoked"
        return Response(
            {"message": f"Permission has been {action} for user ID {user_id}."},
            status=status.HTTP_200_OK
        )