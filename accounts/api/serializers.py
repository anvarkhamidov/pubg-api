from django.contrib.auth import get_user_model
from rest_framework import serializers

Player = get_user_model()


class CustomPlayerDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ("url", "id", "first_name", "username", "email", "image", "balance", "revenue", "matches", "favorites")
