from django.urls import path, include
from rest_framework import routers
from tournament.api.views import TournamentViewSet, PremiumTournamentsViewSet, PrizeViewSet, PlayerViewSet, \
    TicketViewSet

router = routers.DefaultRouter()
router.register('tournament/premium', PremiumTournamentsViewSet, 'premium')
router.register('tournament', TournamentViewSet, 'tournament')
router.register('player', PlayerViewSet, 'player')
router.register('prize', PrizeViewSet)
router.register('ticket', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
