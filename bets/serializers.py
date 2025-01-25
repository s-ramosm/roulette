from rest_framework import serializers
from .models import Bet

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['id', 'user', 'roulette', 'amount', 'number', 'color']
