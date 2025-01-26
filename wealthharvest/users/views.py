from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class RegisterView(APIView):
    """
    API view to handle user registration.

    Methods:
        post(request): Handles the creation of a new user.
    """

    def post(self, request):
        """
        Create a new user with the provided data.

        Args:
            request (Request): The incoming HTTP request containing user data.

        Returns:
            Response: Success or error response.
        """
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
