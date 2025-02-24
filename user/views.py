from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .services.user_service import UserService


class UserSignupView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated users to sign up

    def post(self, request):
        data = request.data
        user = UserService.register_user(
            auth0_id=data["auth0Id"],
            email=data["emailAddress"],
            username=data["fullName"],
        )
        return Response({"message": "User registered successfully!", "user_id": user.id}, status=status.HTTP_201_CREATED)
