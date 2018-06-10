from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from .serializers import PlayerSerializer 
from .models import Player

# Create your views here.
@api_view(['GET'])
def index(request, format=None):
    return Response({
       'players': 'http://localhost:8000/api/v1/players',
    })

class PlayerViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all()

        player_name = self.request.query_params.get('name', None)
        player_age = self.request.query_params.get('age', None )
        player_potential = self.request.query_params.get('potential', None)
        player_overall = self.request.query_params.get('overall_rating', None)
        player_positions = self.request.query_params.get('positions', None)

        if player_name is not None:
            queryset = queryset.filter(name__icontains = player_name)
        if player_age is not None:
            queryset = queryset.filter(age = player_age)
        if player_potential is not None:
            queryset = queryset.filter(potential = player_potential)
        if player_overall is not None:
            queryset = queryset.filter(overall_rating = player_overall)
        if player_positions is not None:
            queryset = queryset.filter(positions__icontains = player_positions)

        return queryset