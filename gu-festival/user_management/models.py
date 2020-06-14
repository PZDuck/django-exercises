from django.db import models
from django.contrib.auth.models import User

# User Profile model, incomplete. Requires: additional info, profile page
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"{self.user}\'s Profile'"
    
# IN CONSIDERATION
# class Band(models.Model):
#     band_name = models.CharField(max_length=255)
#     band_member = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
