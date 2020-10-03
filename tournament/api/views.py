from rest_framework import viewsets
from tournament.models import Tournament, Game
from tournament.api.serializers import TournamentSerializer, GameSerializer


class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class TournamentViewSet(viewsets.ViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
