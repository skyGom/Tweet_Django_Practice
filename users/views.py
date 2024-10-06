from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer
from tweets.serializers import TweetSerializer

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

class UserDetailView(APIView):
    def get_user(self, user_id):
        try:
            return User.objects.get(username=user_id)
        except User.DoesNotExist:
            raise NotFound
        
    def get(self, request, user_id):
        serializer = UserDetailSerializer(self.get_user(user_id))
        return Response(serializer.data)

class UserTweetsView(UserDetailView):
    def get(self, request, user_id):
        serializer = TweetSerializer(self.get_user(user_id).tweets.all(), many=True)
        return Response(serializer.data)