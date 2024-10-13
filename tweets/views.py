from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from .models import Tweet
from .serializers import TweetSerializer

class TweetsListView(APIView):
    
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TweetDetailView(APIView):
    
    def get_tweet(self, tweet_pk):
        try:
            return Tweet.objects.get(pk=tweet_pk)
        except Tweet.DoesNotExist:
            raise NotFound
        
    def get(self, request, tweet_pk):
        serializer = TweetSerializer(self.get_tweet(tweet_pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, tweet_pk):
        tweet = self.get_tweet(tweet_pk)
        serializer = TweetSerializer(tweet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, tweet_pk):
        tweet = self.get_tweet(tweet_pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)