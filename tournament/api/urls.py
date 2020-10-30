from django.urls import path, include
from rest_framework import routers
from tournament.api import views

router = routers.DefaultRouter()
router.register('tournament/premium', views.PremiumTournamentsViewSet, 'premium')
router.register('tournament/today', views.TodayTournamentViewSet, 'today-tournament')
router.register('tournament/upcoming', views.UpcomingTournamentViewSet, 'upcoming-tournament')
router.register('tournament', views.TournamentViewSet, 'tournament')
router.register('player', views.PlayerViewSet, 'player')
router.register('prize', views.PrizeViewSet)
router.register('ticket', views.TicketViewSet)

urlpatterns = [
    path('ticket/buy/<int:id>/', views.BuyTicketView.as_view()),
    path('', include(router.urls)),
]
