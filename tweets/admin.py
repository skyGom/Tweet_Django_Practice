from django.contrib import admin
from .models import Tweet, Like

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """Tweet Admin Definition"""
    
    list_display = ("user", "payload", "likes_count", "created_at",)
    list_filter = ("user",)
    
    def likes_count(self, tweet):
        return tweet.likes.count()
    likes_count.short_description = "Like Count"

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Like Admin Definition"""
    
    list_display = ("user", "tweet",)
    list_filter = ("user",)