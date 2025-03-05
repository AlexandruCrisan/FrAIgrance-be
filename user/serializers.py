# users/serializers.py
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from generate.serializers import StorySerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Disable `jti` check (not present in Auth0 tokens)
        return data


class UserSerializer(serializers.ModelSerializer):
    stories = StorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'credits', 'username', 'email', 'stories']
