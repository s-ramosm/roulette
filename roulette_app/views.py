from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Roulette
from .serializers import RouletteSerializer
from rest_framework.decorators import action
from bets.models import Bet
import random
from django.db.models import Q

# Create your views here.
class RouletteViewSet(ModelViewSet):
    """
    A ViewSet for listing and creating Roulette instances.
    """
    queryset = Roulette.objects.all()
    serializer_class =  RouletteSerializer

    def get_win_bets(self, roulette):
        
        win_number = random.choice([0, 36])
        
        #Get color since number
        if win_number % 2 == 0 : 
            color = "Red"
        else:
            color =  "Black"
        
        #Get Winner
        winning_bets =  Bet.objects.filter(
            Q( Q(number = win_number) | Q( Q(color = color) , Q(number__isnull = True) ) ), 
            roulette = roulette,
        )

        response = []

        for bet in winning_bets:
            bet.set_win_state(win_number)
            response.append(
                {
                    "id" : bet.id,
                    "user_id" : bet.user.id,
                    "winning_amount" : bet.winning_amount
                }
            )

        return response


    def create(self, request):
        """
        Create a new roulette.
        """
        serializer = RouletteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def open(self, request, pk=None):
        
        roulette = self.get_object()
        roulette.state =  "Open"
        roulette.save()

        return Response({"status" :  "open" }, status=200)
    
    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        
        roulette = self.get_object()

        #Check if roulette is closed
        if roulette.state == roulette.CLOSE: return Response({"msg" : "Roulette Already Closed"}, status=400 ) 


        #Close Roulette and check winners 
        roulette.state =  "Close"
        roulette.save()    
        winning_bets = self.get_win_bets(roulette)

        return Response({"winners" :  winning_bets }, status=200)