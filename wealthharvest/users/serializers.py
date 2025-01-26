from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    Handles validation and creation of new users.
    """
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user instance.

        Args:
            validated_data (dict): Validated data from the request.

        Returns:
            User: The created User object.
        """
        
        user = User.objects.create_user(**validated_data)
        return user
