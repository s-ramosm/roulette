from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Roulette
from .serializers import RouletteSerializer

# Create your views here.
class RouletteViewSet(ViewSet):
    """
    A ViewSet for listing and creating Roulette instances.
    """

    def list(self, request):
        """
        List all the roulettes.
        """
        roulettes = Roulette.objects.all()
        serializer = RouletteSerializer(roulettes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new roulette.
        """
        serializer = RouletteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)