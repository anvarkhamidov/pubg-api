from django.urls import path, include
from rest_framework import routers
from tournament.api.views import TournamentViewSet, GameViewSet

router = routers.DefaultRouter()
router.register('tournament', TournamentViewSet)
router.register('game', GameViewSet)

urlpatterns = [
    path('', include(router.urls))
]
