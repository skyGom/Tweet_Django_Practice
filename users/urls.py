from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<str:user_id>/", views.UserDetailView.as_view()),
    path("<str:user_id>/tweets", views.UserTweetsView.as_view()),
]