from rest_framework_mongoengine import serializers
from .models import Player

class PlayerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Player
        fields = '__all__'