from django.db import models
from common.models import CommonModel

class Tweet(CommonModel):
    """Tweet Model Definition"""
    payload = models.TextField(max_length=180,)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="tweets",)
    like = models.ManyToManyField("tweets.Like", related_name="tweets", blank=True,)
    
    def __str__(self):
        return f"{self.user} says: {self.payload}"
    
class Like(CommonModel):
    """Like Model Definition"""
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="likes",)
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE, related_name="likes",)
    
    def __str__(self):
        return f"{self.user} likes {self.tweet}"