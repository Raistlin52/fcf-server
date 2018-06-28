from django.contrib.auth.models import User
from rest_framework import viewsets, status
from football import models
from football import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class GamesOfTheWeek(APIView):
    """
    List all the game data for a particular week
    """
    queryset = models.Game.objects.all()

    def get(self, request, week_id, format=None):
        games = models.Game.objects.filter(week_id=week_id)
        serializer = serializers.GameSerializer(games, many=True)
        return Response(serializer.data)
    

class GamesWithID(APIView):
    """
    List all the game data for a particular week
    """
    queryset = models.Game.objects.all()

    def get(self, request, format=None):
        games = models.Game.objects.all()

        updatedresponse = {}
        for g in games:
            serializer = serializers.GameSerializer(g)
            updatedresponse[g.id] = serializer.data

        print(updatedresponse)
        return Response(updatedresponse)
    

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    pagination_class = None

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer

class WeekViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Week.objects.all()
    serializer_class = serializers.WeekSerializer

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class HistoricBankrollViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HistoricBankroll.objects.all()
    serializer_class = serializers.HistoricBankrollSerializer

class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer