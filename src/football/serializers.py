from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from football.models import Game

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

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