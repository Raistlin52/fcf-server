from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from football.models import Game
from football.serializers import GameSerializer, UserSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer