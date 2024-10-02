from django.shortcuts import render
from .models import Tweet


def tweets_list(request):
    tweets = Tweet.objects.all()
    return render(
        request, "all_tweets.html", {"tweets": tweets, "title": "Hi! all tweets here!"}
    )
    
def tweet_detail(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        return render(request, "tweet_detail.html", {"tweet": tweet})
    except Tweet.DoesNotExist:
        return render(request, "tweet_detail.html", {"not_found": True})    