from django.urls import path, include
from rest_framework import routers

from tournament.api.views import PremiumTournamentsViewSet, TournamentViewSet, PrizeViewSet, PlayerViewSet, \
    TicketViewSet

router = routers.DefaultRouter()
router.register('tournament/premium', PremiumTournamentsViewSet, 'premium')
router.register('tournament', TournamentViewSet, 'tournament')
router.register('prize', PrizeViewSet)
router.register('player', PlayerViewSet)
router.register('ticket', TicketViewSet)


urlpatterns = [
    path("accounts/", include("accounts.api.urls")),
    path('', include(router.urls)),
    # path("tournaments/", include("tournament.api.urls")),
]
