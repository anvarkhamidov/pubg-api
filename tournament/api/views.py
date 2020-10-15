from django.contrib.auth import get_user_model
from rest_framework import viewsets, request

from tournament.models import Tournament, Prize, Ticket
from tournament.api.serializers import TournamentSerializer, PrizeSerializer, PlayerSerializer, TicketSerializer

Player = get_user_model()


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class PremiumTournamentsViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.filter(is_premium=True).all()
    serializer_class = TournamentSerializer


class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
