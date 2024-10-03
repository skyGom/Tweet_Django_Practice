from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_list),
    path("<str:user_id>/", views.user_detail),
    path("<str:user_id>/tweets", views.user_tweets),
]