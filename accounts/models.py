from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    favourite_games = models.TextField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
