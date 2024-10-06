from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer

class TweetsListView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

class TweetDetailView(APIView):
    def get_tweet(self, tweet_pk):
        try:
            return Tweet.objects.get(pk=tweet_pk)
        except Tweet.DoesNotExist:
            raise NotFound
        
    def get(self, request, tweet_pk):
        serializer = TweetSerializer(self.get_tweet(tweet_pk))
        return Response(serializer.data)