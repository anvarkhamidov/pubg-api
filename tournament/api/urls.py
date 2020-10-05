from django.urls import path, include
from rest_framework import routers
from tournament.api.views import TournamentViewSet

router = routers.DefaultRouter()
router.register('tournament', TournamentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
