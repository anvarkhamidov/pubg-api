from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

Player = get_user_model()


class Tournament(models.Model):
    name = models.CharField(max_length=100, help_text='The public name of the tournament')
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        """
        Make a slug from Tournament.name
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100, help_text='The public name of the tournament')
    slug = models.SlugField(max_length=100)
    kill_revenue = models.FloatField(default=0)
    cost = models.FloatField()
    max_players = models.IntegerField()
    players = models.ManyToManyField(Player)
