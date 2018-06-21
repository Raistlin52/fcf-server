from django.contrib.auth.models import User
from rest_framework import viewsets
from football import models
from football import serializers


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

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