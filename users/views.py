from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserListSerializer, PrivateUserDetailSerializer
from tweets.serializers import TweetSerializer
from django.contrib.auth import authenticate, login, logout

class UserListView(APIView):
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        
        serializer = PrivateUserDetailSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class UserDetailView(APIView):
    
    def get_user(self, user_pk):
        try:
            return User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise NotFound
        
    def get(self, request, user_pk):
        serializer = PrivateUserDetailSerializer(self.get_user(user_pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserTweetsView(UserDetailView):
    
    def get(self, request, user_pk):
        serializer = TweetSerializer(self.get_user(user_pk).tweets.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserChangePasswordView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        
        if not old_password or not new_password:
            raise ParseError
        
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError
        
class UserLogInView(APIView):
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            raise ParseError
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return Response(
                {"ok": "Welcome, {}!".format(username)},
                status=status.HTTP_200_OK,
                )
        return Response(
            {"error": "Invalid username or password."},
            status=status.HTTP_401_UNAUTHORIZED,
            )
    
class UserLogOutView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK,)