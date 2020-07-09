from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Represents model user and for 'id', 'username', and 'email' field
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    # Model Serializer used with model creation
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # used when doing serializer.save() in api.py
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()
        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    # You can validate a specific field by using def validate_<fieldname>
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user

        raise serializers.ValidationError("Incorrect Credentials")
