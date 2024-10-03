from rest_framework import serializers

class UserListSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        read_only=True,
    )
    
    gender = serializers.CharField(
        max_length=10,
        read_only=True,
    )
    
    legion = serializers.CharField(
        max_length=40,
        read_only=True,
    )

class UserDetailSerializer(serializers.Serializer):
    
    pk = serializers.IntegerField(
        read_only=True,
    )
    
    first_name = serializers.CharField(
        max_length=150,
        read_only=True,
    )
    
    last_name = serializers.CharField(
        max_length=150,
        read_only=True,
    )
    
    name = serializers.CharField(
        max_length=150,
        read_only=True,
    )
    
    gender = serializers.CharField(
        max_length=10,
        read_only=True,
    )
    
    legion = serializers.CharField(
        max_length=40,
        read_only=True,
    )