from rest_framework import serializers
from .models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "gender",
            "legion",
        ]

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "gender",
            "legion",
        ]