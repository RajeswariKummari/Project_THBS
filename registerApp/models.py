from django.db import models
from django.contrib.auth.models import User


class Readlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.JSONField()
    # title = models.CharField(max_length=255)
    # authors = models.CharField(max_length=255)

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.JSONField()
    # title = models.CharField(max_length=255)
    # authors = models.CharField(max_length=255)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add any additional fields you need for the user profile
#     # For example, you can add fields like date_of_birth, profile_picture, etc.

#     def __str__(self):
#         return self.user.username





