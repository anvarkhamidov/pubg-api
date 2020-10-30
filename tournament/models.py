from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import Player, CoreModel


class Prize(CoreModel):
    name = models.CharField(max_length=100, help_text='The name of prize')
    icon = models.ImageField(default='default_prize.jpg')
    price = models.FloatField(blank=True, null=True, help_text='Price')


class Tournament(models.Model):
    name = models.CharField(max_length=100, help_text='The public name of the tournament')
    slug = models.SlugField(max_length=100)
    image = models.ImageField(default='default_tournament.jpg')
    description = models.TextField(help_text='Match info')
    instructions = models.TextField(help_text='Match Instructions')
    password = models.CharField(max_length=100, help_text='Password for tournament')
    kill_revenue = models.FloatField(default=0, help_text='Kill revenue')
    starts_at = models.DateTimeField(auto_now=False)
    prizes = models.ManyToManyField('tournament.Prize')
    cost = models.FloatField(default=0, help_text='Match cost')
    is_premium = models.BooleanField(default=False, help_text='Premium match')
    max_players = models.PositiveIntegerField(default=100, 
                                              validators=[MinValueValidator(2), MaxValueValidator(100)])
    players = models.ManyToManyField('accounts.Player')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Make a slug from Tournament.name"""
        self.slug = slugify(self.name)
        self.starts_at = timezone.make_aware(self.starts_at)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'


class Ticket(CoreModel):
    player = models.ForeignKey('accounts.Player', on_delete=models.DO_NOTHING)
    tournament = models.ForeignKey('tournament.Tournament', on_delete=models.DO_NOTHING)
    cost = models.FloatField()

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
