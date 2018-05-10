from .models import Game
import rest_framework.serializers as serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
          'id',
          'week',
          'away',
          'home',
          'game_time',
          'network',
          'money_line_home',
          'money_line_away',
          'spread_home',
          'over_under',
          'away_final',
          'home_final'
        )