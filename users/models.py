from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User Model"""

    class GenderChoices(models.TextChoices):
        """Gender Choices"""
        male = (
            "male",
            "Male",
        )
        female = ("female", "Female")
    
    class LegionChoices(models.TextChoices):
        """Legion Choices"""
        ko = "ko", "South Korea"
        usa = "usa", "United States of America"
        jp = "jp", "japan"
        uk = "uk", "United Kingdom"
        tw = "tw", "Taiwan"
        si = "si", "Singapore"
        gm = "gm", "Germany"
        fr = "fr", "France"
        it = "it", "Italy"
        ca = "ca", "Canada"
        
    nick_name = models.CharField(max_length=20, blank=True, editable=False,)
    first_name = models.CharField(max_length=30, blank=True, editable=False,)
    last_name = models.CharField(max_length=30, blank=True, editable=False,)
    image = models.ImageField(blank=True, null=True,)
    gender = models.CharField(
        max_length=10,
        default="",
        choices=GenderChoices.choices,
    )
    legion = models.CharField(
        max_length=40,
        default="",
        choices=LegionChoices.choices,
    )
    
        
    