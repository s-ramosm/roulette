from rest_framework import serializers
from .models import Roulette

class RouletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roulette
        fields = '__all__'