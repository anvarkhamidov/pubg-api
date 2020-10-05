from rest_framework import viewsets
from tournament.models import Tournament
from tournament.api.serializers import TournamentSerializer


class TournamentViewSet(viewsets.ViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
