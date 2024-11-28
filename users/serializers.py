from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Password is write-only
        }

    def validate(self, data):
        # Validate if 'author' or 'admin' requires 'is_permitted' to be False
        user_type = data.get('user_type', 'user')
        is_permitted = data.get('is_permitted', True)  # Default is True
        if user_type in ['author', 'admin'] and is_permitted:
            raise serializers.ValidationError(
                f"Users with type '{user_type}' cannot have 'is_permitted' set to True."
            )
        return data

    def create(self, validated_data):
        # Create a new user instance
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
