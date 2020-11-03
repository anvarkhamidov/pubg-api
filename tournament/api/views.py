from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets, status

from datetime import datetime, date, timedelta, time

from accounts.api.serializers import CustomPlayerDetailsSerializer
from config.views import APIViewMixin
from tournament.models import Tournament, Prize, Ticket
from tournament.api.serializers import TournamentSerializer, PrizeSerializer, TicketSerializer

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


class TodayTournamentViewSet(viewsets.ModelViewSet):
    date = datetime.combine(timezone.now(), time.min)
    queryset = Tournament.objects.filter(starts_at__date=date).all()
    serializer_class = TournamentSerializer


class UpcomingTournamentViewSet(viewsets.ModelViewSet):
    start_date = datetime.combine(timezone.now() + timedelta(days=1), time.min)
    queryset = Tournament.objects.filter(starts_at__gte=start_date).all()
    serializer_class = TournamentSerializer


class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = CustomPlayerDetailsSerializer


class BuyTicketView(APIViewMixin):
    def post(self, request, id):
        tournament = Tournament.objects.filter(id=id).first()
        current_user = request.user
        
        if tournament:
            tournament.players.add(current_user)
            tournament.max_players -= 1
            tournament.save()
            tournament_serializer = TournamentSerializer(tournament, context={'request': request})

            ticket = Ticket(player=current_user, tournament=tournament, cost=tournament.cost)
            ticket.save()
            ticket_serializer = TicketSerializer(ticket, context={'request': request})

            data = {'tournament': tournament_serializer.data, 'ticket': ticket_serializer.data}
            status = status.HTTP_200_OK
        
        else:
            data = {'error': 'Wrong tournament ID.'}
            status = status.HTTP_400_BAD_REQUEST

        
        return Response(data, status=status)