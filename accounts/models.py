from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from tournament.models import Tournament


class Player(AbstractUser):
    email = models.EmailField(_('email address'), blank=False)
    balance = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
    matches = models.IntegerField(default=0)
    favorites = models.ManyToManyField('tournament.Tournament')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
