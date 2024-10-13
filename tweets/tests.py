from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User

class TweetTests(APITestCase):
    
    test_payload = "This is test tweet"
    tweets_url = "/api/v1/tweets/"
    tweet_detail_url = "/api/v1/tweets/1"
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            )
        self.tweet = Tweet.objects.create(
            payload=self.test_payload,
            user=self.user,
            )
        
    def test_get_tweets(self):
        response = self.client.get(self.tweets_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['payload'], self.test_payload)
        
    def test_create_tweet(self):
        new_payload = "This is another test tweet"
        response = self.client.post(self.tweets_url, {'payload': new_payload, 'user': self.user.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 2)
        self.assertEqual(response.data['payload'], new_payload)
        
    def test_get_tweet_detail(self):
        response = self.client.get(self.tweet_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payload'], self.test_payload)
        
    def test_update_tweet(self):
        update_tweet = "This is Updated tweet"
        response = self.client.put(self.tweet_detail_url, {'payload': update_tweet, 'user': self.user.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payload'], update_tweet)
        
    def test_delete_tweet(self):
        response = self.client.delete(self.tweet_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tweet.objects.count(), 0)
        

