# from django.contrib.auth import get_user_model
from collections import defaultdict
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from accounts.models import Player

# Player = get_user_model()


class Prize(models.Model):
    name = models.CharField(max_length=100, help_text='The name of prize')
    icon = models.ImageField(default='default_prize.jpg')
    price_per_kill = models.FloatField(blank=True, null=True, help_text='Price per kill')
    winner_price = models.FloatField(blank=True, null=True, help_text='Price for winner at the end')
    price_for_top_winners = models.FloatField(blank=True, null=True, help_text='Price for top players')


class Tournament(models.Model):
    name = models.CharField(max_length=100, help_text='The public name of the tournament')
    slug = models.SlugField(max_length=100)
    image = models.ImageField(default='default_tournament.jpg')
    description = models.TextField(help_text='Match info')
    instructions = models.TextField(help_text='Match Instructions')
    password = models.CharField(max_length=100, help_text='Password for tournament')
    kill_revenue = models.FloatField(default=0, help_text='Kill revenue')
    created_at = models.DateTimeField(default=datetime.now)
    start_at = models.DateTimeField()
    prizes = models.ManyToManyField(Prize)
    cost = models.FloatField(default=0, help_text='Match cost')
    is_premium = models.BooleanField(default=False, help_text='Premium match')
    max_players = models.PositiveIntegerField(default=100, 
                                              validators=[MinValueValidator(2), MaxValueValidator(100)])
    players = models.ManyToManyField(Player)

    def save(self, *args, **kwargs):
        """Make a slug from Tournament.name"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'


class Ticket(models.Model):
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    cost = models.FloatField()

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
