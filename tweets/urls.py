from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweets_list,),
    path("<int:tweet_pk>", views.tweet_detail,),
]
