from django.contrib import admin
from .models import Tweet, Like

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """Tweet Admin Definition"""
    
    list_display = ("user", "payload",)
    list_filter = ("user",)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Like Admin Definition"""
    
    list_display = ("user", "tweet",)
    list_filter = ("user",)