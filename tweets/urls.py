from django.urls import path
from . import views

urlpatterns = [
    path("", views.TweetsListView.as_view()),
    path("<int:tweet_pk>", views.TweetDetailView.as_view()),
]
