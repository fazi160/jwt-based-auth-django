from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from utils.decorators import custom_auth_required


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AdminAuthorView(APIView):
    
    @custom_auth_required(user_types=['admin'])
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')  
        is_permitted = request.data.get('is_permitted') 

        if user_id is None or is_permitted is None:
            return Response(
                {"error": "Both 'user_id' and 'is_permitted' fields are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        user.is_permitted = is_permitted
        user.save()

        action = "granted" if is_permitted else "revoked"
        return Response(
            {"message": f"Permission has been {action} for user ID {user_id}."},
            status=status.HTTP_200_OK
        )
