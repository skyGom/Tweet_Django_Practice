from django.contrib import admin
from .models import Tweet, Like
from .filter import MuskFilter

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """Tweet Admin Definition"""
    
    list_display = ("user", "payload", "likes_count", "created_at",)
    list_filter = ("created_at", MuskFilter,)
    
    search_fields = ("=user__username", "payload",)
    
    def likes_count(self, tweet):
        return tweet.likes.count()
    likes_count.short_description = "Like Count"

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Like Admin Definition"""
    
    list_display = ("user", "tweet",)
    list_filter = ("created_at",)
    
    search_fields = ("=user__username",)