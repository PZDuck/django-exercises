from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    age = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
