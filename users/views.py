from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer
from tweets.serializers import TweetSerializer

@api_view()
def user_list(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(
        {
            "state": True,
            "users": serializer.data,
        },
    )
    
@api_view()
def user_detail(request, user_id):
    try:
        user = User.objects.get(username=user_id)
        serializer = UserDetailSerializer(user)
        return Response(
            {
                "state": True,
                "user_info": serializer.data,
            },
        )
    except User.DoesNotExist:
        return Response(
            {
                "state": False,
            },
        )
        
@api_view()
def user_tweets(request, user_id):
    try:
        user = User.objects.get(username=user_id)
        all_user_tweets = user.tweets.all()
        serializer = TweetSerializer(all_user_tweets, many=True)
        return Response(
            {
                "state": True,
                "user_tweets": serializer.data,
            },
        )
    except User.DoesNotExist:
        return Response(
            {
                "state": False,
            },
        )