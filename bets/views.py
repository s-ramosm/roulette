from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Bet
from .serializers import BetSerializer
from rest_framework import status


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


    def create(self, request, *args, **kwargs):
        
        user = request.user_from_id
        if not user:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        request.data['user'] = user.id

        number = request.data.get('number')
        color = request.data.get('color')
        if number is not None:
            if number % 2 == 0:
                request.data['color'] = 'Red'  
            else:
                request.data['color'] = 'Black'

        elif color is None:
            return Response({"detail": "Number or Color is required."}, status=status.HTTP_400_BAD_REQUEST)


        return super().create(request, *args, **kwargs)