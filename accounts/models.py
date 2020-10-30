from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(AbstractUser):
    email = models.EmailField(_('email address'), blank=False)
    balance = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
    matches = models.IntegerField(default=0)
    image = models.ImageField(default='default_avatar.jpg')
    # favorites = models.ManyToManyField('tournament.Tournament')
    background_image = models.ImageField(default='default_tournament.jpg')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class VerificationToken(CoreModel):
    token = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.email} - {self.token}"