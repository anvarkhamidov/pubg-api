from rest_framework import serializers
from tournament.models import Tournament, Prize, Ticket
from accounts.models import Player
from accounts.api.serializers import CustomPlayerDetailsSerializer


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class PrizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prize
        fields = "__all__"


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ("url", "id", "first_name", "username", "email", "balance", "revenue", "matches", "favorites")


class TournamentSerializer(serializers.ModelSerializer):
    players = CustomPlayerDetailsSerializer(many=True, read_only=True)
    prizes = PrizeSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'tournament-detail'},
        }
