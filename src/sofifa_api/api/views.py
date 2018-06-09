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
        return queryset