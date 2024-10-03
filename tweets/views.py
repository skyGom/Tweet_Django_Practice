from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer

@api_view()
def tweets_list(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(
        {
            "state": True,
            "tweets": serializer.data,
        },
    )

@api_view()
def tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
        serializer = TweetSerializer(tweet)
        return Response(
            {
                "state": True,
                "tweet": serializer.data,
            },
        )
    except Tweet.DoesNotExist:
        return Response(
            {
                "state": False,
            },
        )  