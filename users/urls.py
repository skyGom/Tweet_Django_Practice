from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<int:user_pk>/", views.UserDetailView.as_view()),
    path("<int:user_pk>/tweets", views.UserTweetsView.as_view()),
    path("password", views.UserChangePasswordView.as_view()),
    path("login", views.UserLogInView.as_view()),
    path("logout", views.UserLogOutView.as_view()),
]